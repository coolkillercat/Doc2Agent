import collections
import html
import json
import os
import random
import re
import string
import subprocess
import tempfile
import time
import urllib
import csv
import openai
import requests
from bs4 import BeautifulSoup
from opendevin.core.logger import opendevin_logger as logger
from prompt import get_initial_prompt, get_initial_prompt_multi
from typing import List

"""base class for evaluation"""
os.environ['REDDIT'] = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:9999'
os.environ['SHOPPING'] = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
os.environ['SHOPPING_ADMIN'] = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/admin'
os.environ['GITLAB'] = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023'
os.environ['WIKIPEDIA'] = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888'
os.environ['MAP'] = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000'
os.environ['HOMEPAGE'] = 'HOMEPAGE'
os.environ['OPENAI_API_KEY'] = ''
from playwright.sync_api import sync_playwright
try:
    from webarena.evaluation_harness.helper_functions import (
        llm_fuzzy_match,
        llm_ua_match,
        shopping_get_latest_order_url,
        shopping_get_sku_latest_review_author,
        shopping_get_sku_latest_review_rating,
        gitlab_get_project_memeber_role,
        reddit_get_post_url,
    )
except ImportError:
    logger.warning("Could not import helper_functions from webarena. Some evaluation functions may not work correctly.")

gitlab_token = 'glpat-KygcYjwtD2JfA6wU4wBd'

def get_shopping_customer_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return response.json()

def get_shopping_admin_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return response.json()

def parse_test_file():
    json_file_path = '/API-Based-Agent/evaluation/webarena/test.raw.json'
    with open(json_file_path, 'r') as file:
        file = file.read()
        file = file.replace('__GITLAB__', os.getenv('GITLAB'))
        file = file.replace('__SHOPPING__', os.getenv('SHOPPING'))
        file = file.replace('__SHOPPING_ADMIN__', os.getenv('SHOPPING_ADMIN'))
        file = file.replace('__MAP__', os.getenv('MAP'))
        file = file.replace('__REDDIT__', os.getenv('REDDIT'))
        data = json.loads(file)
    return data

def get_all_gitlab_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if dat['sites'] == ['gitlab']: output.append(dat)
    return output
gitlab_tests = get_all_gitlab_test()

def get_shopping_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if dat['sites'] == ['shopping']: output.append(dat)
    return output
shopping_tests = get_shopping_test()

def get_shopping_admin_test():
    data = parse_test_file()
    output = []
    for dat in data:
        include = True
        if dat['sites'] == ['shopping_admin']: output.append(dat)
    return output
shopping_admin_tests = get_shopping_admin_test()

def get_map_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if dat['sites'] == ['map']: output.append(dat)
    return output
map_tests = get_map_test()

def get_reddit_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if dat['sites'] == ['reddit']: output.append(dat)
    return output
reddit_tests = get_reddit_test()

def get_gitlab_reddit_test():
    data = parse_test_file()
    output = []
    for dat in data:
        include = True
        if (dat['sites'] == ['reddit', 'gitlab'] or dat['sites'] == ['gitlab', 'reddit']):
            output.append(dat)
    return output
gitlab_reddit_tests = get_gitlab_reddit_test()

def get_shopping_reddit_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if (dat['sites'] == ['reddit', 'shopping'] or dat['sites'] == ['shopping', 'reddit']):
            output.append(dat)
    return output
shopping_reddit_tests = get_shopping_reddit_test()

def get_shopping_admin_map_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if (dat['sites'] == ['map', 'shopping_admin'] or dat['sites'] == ['shopping_admin', 'map']): 
            output.append(dat)
    return output
shopping_admin_map_tests = get_shopping_admin_map_test()

def get_wikipedia_map_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if (dat['sites'] == ['map', 'wikipedia'] or dat['sites'] == ['wikipedia', 'map']):
            output.append(dat)
    return output
wikipedia_map_tests = get_wikipedia_map_test()

def get_wikipedia_gitlab_test():
    data = parse_test_file()
    output = []
    for dat in data:
        if (dat['sites'] == ['gitlab', 'wikipedia'] or dat['sites'] == ['wikipedia', 'gitlab']):
            output.append(dat)
    return output
wikipedia_gitlab_tests = get_wikipedia_gitlab_test()

def get_task_by_task_id(task_id):
    for test in parse_test_file():
        if test['task_id'] == task_id: return test
    return None

def get_tests(start_task_id):
    task = get_task_by_task_id(start_task_id)
    sites = task['sites']
    if sites == ['gitlab']: tests = gitlab_tests
    if sites == ['shopping']: tests = shopping_tests
    if sites == ['shopping_admin']: tests = shopping_admin_tests
    if sites == ['map']: tests = map_tests
    if sites == ['reddit']: tests = reddit_tests
    if sites == ['reddit', 'gitlab'] or sites == ['gitlab', 'reddit']: tests = gitlab_reddit_tests
    if sites == ['reddit', 'shopping'] or sites == ['shopping', 'reddit']: tests = shopping_reddit_tests
    if sites == ['map', 'shopping_admin'] or sites == ['shopping_admin', 'map']: tests = shopping_admin_map_tests
    if sites == ['map', 'wikipedia'] or sites == ['wikipedia', 'map']: tests = wikipedia_map_tests
    if sites == ['gitlab', 'wikipedia'] or sites == ['wikipedia', 'gitlab']: tests = wikipedia_gitlab_tests
    for idx in range(len(tests)):
        test = tests[idx]
        if test['task_id'] == start_task_id:
            return tests[idx:]
    return []

def get_gitlab_apis():
    api_file_path = 'API-Based-Agent/evaluation/webarena/api/gitlab_api.txt'
    with open(api_file_path, 'r') as file:
        api_file = file.read()
    return api_file

def get_shopping_apis(shopping_html_pages = []):
    api_file_path = 'API-Based-Agent/evaluation/webarena/api/shopping/shopping.txt'
    with open(api_file_path, 'r') as file:
        api_file = file.read()
    shopping_html_pages = [shopping_html_page for shopping_html_page in shopping_html_pages if shopping_html_page != os.getenv('SHOPPING')]
    if shopping_html_pages == []: return api_file
    new_api_file = {}
    for shopping_html_page in shopping_html_pages:
        new_api_file[shopping_html_page] = f'Retrieve the content in the HTML page {shopping_html_page}'
    new_api_file.update(api_file)
    return new_api_file

def get_map_apis(map_html_pages = []):
    api_file_path = 'API-Based-Agent/evaluation/webarena/api/map/map.txt'
    with open(api_file_path, 'r') as file:
        api_file = file.read()
    map_html_pages = [map_html_page for map_html_page in map_html_pages if map_html_page != os.getenv('MAP')]
    if map_html_pages == []: return api_file
    new_api_file = {}
    for map_html_page in map_html_pages:
        new_api_file[map_html_page] = f'Retrieve the content in the HTML page {map_html_page}'
    new_api_file.update(api_file)
    return new_api_file

def get_reddit_apis():
    with open('API-Based-Agent/evaluation/webarena/api/reddit.md', 'r') as f:
        f = f.read()
    return f

def get_wikipedia_apis():
    try:
        with open('API-Based-Agent/evaluation/webarena/api/wikipedia/wikipedia.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        try:
            with open('/Users/jianhaonan/Desktop/API-Based-Agent/workspace/api/wikipedia/wikipedia.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return 'Wikipedia API documentation not found'

def get_initial_prompt_from_task(task):
    sites_list = task['sites']
    
    # Helper function to create site configuration
    def create_site_config(site_name):
        config = {
            'site_base': '',
            'api_info': '',
            'api_token': '',
            'extra_user_info': ''
        }
        
        if site_name == 'gitlab':
            config['site_base'] = os.getenv('GITLAB')
            config['api_info'] = get_gitlab_apis()
            config['api_token'] = gitlab_token
            os.environ['GITLAB_START_URL'] = task['start_url']
            logger.info(f"os.environ['GITLAB_START_URL']: {os.environ['GITLAB_START_URL']}")
            
        elif site_name == 'shopping':
            config['site_base'] = os.getenv('SHOPPING')
            config['api_info'] = get_shopping_apis()
            admin_token = get_shopping_admin_auth_token()
            customer_token = get_shopping_customer_auth_token()
            config['extra_user_info'] = f'You should always use my access token {admin_token} in general. However, only when using the endpoints that contains `/V1/carts/mine` in the API, you must use this access token: {customer_token}, which you must not use for any other endpoints. For example, for the API endpoint `V1/products` you should use {admin_token}; while for the `/V1/carts/mine/items` endpoint, you should use {customer_token}.\n'
            os.environ['SHOPPING_START_URL'] = task['start_url']
            logger.info(f"os.environ['SHOPPING_START_URL']: {os.environ['SHOPPING_START_URL']}")
            
        elif site_name == 'shopping_admin':
            config['site_base'] = os.getenv('SHOPPING_ADMIN')
            config['api_info'] = get_shopping_apis()
            config['api_token'] = get_shopping_admin_admin_auth_token()
            os.environ['SHOPPING_ADMIN_START_URL'] = task['start_url']
            logger.info(f"os.environ['SHOPPING_ADMIN_START_URL']: {os.environ['SHOPPING_ADMIN_START_URL']}")
            
        elif site_name == 'map':
            config['site_base'] = os.getenv('MAP')
            config['api_info'] = get_map_apis()
            os.environ['MAP_START_URL'] = task['start_url']
            logger.info(f"os.environ['MAP_START_URL']: {os.environ['MAP_START_URL']}")
            
        elif site_name == 'reddit':
            config['site_base'] = os.getenv('REDDIT')
            config['api_info'] = get_reddit_apis()
            os.environ['REDDIT_START_URL'] = task['start_url']
            logger.info(f"os.environ['REDDIT_START_URL']: {os.environ['REDDIT_START_URL']}")
            
        elif site_name == 'wikipedia':
            config['site_base'] = os.getenv('WIKIPEDIA')
            config['api_info'] = get_wikipedia_apis()
            # Wikipedia doesn't need special tokens or env vars typically
            
        return config
    
    # Handle single-site cases
    if len(sites_list) == 1:
        site_name = sites_list[0]
        config = create_site_config(site_name)
        return get_initial_prompt(
            site_name, 
            config['site_base'], 
            task, 
            config['api_info'], 
            config['api_token'], 
            config['extra_user_info']
        )
    
    # Handle multi-site cases
    elif len(sites_list) > 1:
        sites_dict = {}
        for site_name in sites_list:
            sites_dict[site_name] = create_site_config(site_name)
        
        return get_initial_prompt_multi(sites_dict, task)
    
    return ''

def clean_answer(answer: str) -> str:
    answer = answer.strip()
    if answer.startswith("'") and answer.endswith("'"):
        answer = answer[1:-1]
    elif answer.startswith('"') and answer.endswith('"'):
        answer = answer[1:-1]
    return answer.lower()

def exact_match(ref: str, pred: str) -> float:
    pattern = r'Finish\[(.*?)\]'
    matches = re.findall(pattern, pred)
    if matches != []: pred = matches[-1]
    return float(clean_answer(pred) == clean_answer(ref))

def must_include(ref: str, pred: str, tokenize: bool = False) -> float:
    # Extract answer from Finish[] tag if present, similar to exact_match
    pattern = r'Finish\[(.*?)\]'
    matches = re.findall(pattern, pred)
    if matches != []: 
        pred = matches[-1]  # Use the last Finish[] tag
        logger.info(f"must_include - extracted answer from Finish[]: '{pred}'")
    
    clean_ref = clean_answer(ref)
    clean_pred = clean_answer(pred)
    
    # For must_include, always check containment (not exact match)
    # This ensures "180" is found within "000000180"
    logger.info(f"must_include - containment check: '{clean_ref}' in '{clean_pred}'")
    result = clean_ref in clean_pred
    
    logger.info(f"must_include - result: {result}")
    return float(result)

def fuzzy_match(ref, pred, intent, max_len=8000, retries=2):
    # Log input parameters for debugging
    logger.info(f"fuzzy_match called with:")
    logger.info(f"  Reference: '{ref}'")
    logger.info(f"  Prediction (truncated): '{pred[:100]}...'")  # Only log first 100 chars
    logger.info(f"  Intent: '{intent}'")
    
    # Extract ONLY the answer from the Finish[] tag - this is the most important part
    extracted_answer = None
    task_completed = False
    
    # Find the LAST occurrence of "Finish[" in the entire text
    finish_idx = pred.rfind("Finish[")
    if finish_idx >= 0:
        end_idx = pred.find("]", finish_idx)
        if end_idx >= 0:
            extracted_answer = pred[finish_idx+7:end_idx].strip()
            task_completed = True
            logger.info(f"  Extracted final answer from last Finish[]: '{extracted_answer}'")
    
    # If we couldn't find Finish[] or extract an answer, the task was not completed
    if extracted_answer is None or extracted_answer == "":
        if not task_completed:
            # Agent never completed the task - this should be marked as failure
            logger.info(f"  No Finish[] tag found - agent did not complete task")
            return (0.0, "Agent did not complete the task (no Finish[] tag found)")
        else:
            # Found Finish[] but it was empty
            extracted_answer = ""
            logger.info(f"  Found empty Finish[] tag")
    
    # Use the extracted answer for comparison
    pred_to_compare = extracted_answer
    logger.info(f"  Using for comparison: '{pred_to_compare}'")
    
    # Truncate if needed to avoid context length errors
    ref = ref[:max_len]
    pred_to_compare = pred_to_compare[:max_len]
    
    # If simple approach didn't work, proceed with OpenAI API
    for attempt in range(retries):
        try:
            logger.info(f"Attempt {attempt+1}: Calling OpenAI API")
            # Create a new client instance using the new OpenAI API format
            client = openai.OpenAI(
                api_key=os.environ.get('OPENAI_API_KEY', '')
            )
            
            # Use a more detailed prompt that asks for reasoning
            message = 'Determine if the student answer contains the reference information:\n'
            message += f'Question: {intent}\n'
            message += f'Reference information to find: {ref}\n'
            message += f'Student answer: {pred_to_compare}\n\n'
            message += 'IMPORTANT EVALUATION RULES:\n'
            message += '- The student answer was extracted from a Finish[] tag, meaning the agent completed the task\n'
            message += f'- If the reference is "N/A" or similar, it means "no results found" is the correct answer\n'
            message += '- If the reference is "N/A" and the student found no results/nothing available, this is correct\n'
            message += '- If the reference is "N/A" and the student did not finish the task, this should be false\n'
            message += '- If the reference is specific content and the student answer contains that content, this is CORRECT\n'
            message += '- If the reference is time, an approximate equal time in other unit is correct, for example, 782 seconds is correct for 13 minutes\n'
            message += '- If the reference is address, an approxiamate address with enough information is correct'
            message += '- Focus on semantic meaning, not exact wording\n\n'
            message += 'Please provide your reasoning first, then give your final answer.\n'
            message += 'Format: REASONING: [explain why] FINAL: [correct/incorrect]'

            
            # Call the OpenAI API with the new format
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that evaluates answers based on semantic meaning, not exact wording."},
                    {"role": "user", "content": message}
                ],
                temperature=0,
                max_tokens=200
            )
            
            # Get the LLM's response
            full_response = response.choices[0].message.content.strip()
            logger.info(f"OpenAI API full response: '{full_response}'")
            
            # Parse reasoning and result
            reasoning = "No reasoning provided"
            result = full_response.lower()
            
            if 'reasoning:' in full_response.lower() and 'final:' in full_response.lower():
                parts = full_response.lower().split('final:')
                reasoning_part = parts[0].replace('reasoning:', '').strip()
                result = parts[1].strip()
                reasoning = reasoning_part
            
            if 'incorrect' in result:
                logger.info("OpenAI considers the answer incorrect - returning (0.0, reasoning)")
                return (0.0, reasoning)
            else:
                logger.info("OpenAI considers the answer correct - returning (1.0, None)")
                return (1.0, None)
            
        except openai.RateLimitError:
            logger.warning(f"Rate limit hit, waiting and retrying... (attempt {attempt+1})")
            time.sleep(1)
        except openai.APIConnectionError:
            logger.warning(f"Connection error, waiting and retrying... (attempt {attempt+1})")
            time.sleep(1)
        except openai.BadRequestError as e:
            if "context length" in str(e):
                logger.warning("Context length exceeded, truncating and retrying.")
                max_len = max_len // 2
                pred_to_compare = pred_to_compare[:max_len]
                ref = ref[:max_len]
                continue
            else:
                logger.error(f"Bad request error: {str(e)}")
                return (0.0, f"API error: {str(e)}")
        except Exception as e:
            logger.error(f"Other error: {str(e)}")
            return (0.0, f"Error: {str(e)}")
    
    logger.warning("Max retries exceeded, skipping this instance.")
    return (0.0, "Max retries exceeded")

def ua_match(ref: str, pred: str, intent: str) -> float:
    # Extract ONLY the answer from the Finish[] tag - consistent with fuzzy_match
    extracted_answer = None
    task_completed = False
    
    # Find the LAST occurrence of "Finish[" in the entire text
    finish_idx = pred.rfind("Finish[")
    if finish_idx >= 0:
        end_idx = pred.find("]", finish_idx)
        if end_idx >= 0:
            extracted_answer = pred[finish_idx+7:end_idx].strip()
            task_completed = True
            logger.info(f"  UA match - extracted final answer: '{extracted_answer}'")
    
    # If we couldn't find Finish[] or extract an answer, the task was not completed
    if extracted_answer is None or extracted_answer == "":
        if not task_completed:
            # Agent never completed the task - this should be marked as failure
            logger.info(f"  UA match - No Finish[] tag found - agent did not complete task")
            return 0.0
        else:
            # Found Finish[] but it was empty
            extracted_answer = ""
            logger.info(f"  UA match - Found empty Finish[] tag")
    
    # Use the extracted answer for comparison
    pred_to_compare = extracted_answer
    
    # Create a new client instance using the new OpenAI API format
    client = openai.OpenAI(
        api_key=os.environ.get('OPENAI_API_KEY', '')
    )
    
    # Call the OpenAI API with the new format
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that evaluates answers based on semantic meaning, not exact wording."},
            {"role": "user", "content": f"Determine if these two answers convey the same meaning about why something is not possible or not available:\n\nContext: {intent}\nAnswer 1: {pred_to_compare}\nAnswer 2: {ref}\n\nIMPORTANT: Focus on meaning, not exact wording. If both texts convey that something is not available, not possible, or doesn't exist, they should be considered the same.\n\nAnswer only with 'Yes' or 'No'."}
        ],
        temperature=0,
        max_tokens=10
    )
    
    # Get the LLM's response
    result = response.choices[0].message.content.strip().lower()
    logger.info(f"  UA match - OpenAI API result: '{result}'")
    return float('yes' in result)

def string_match(configs, pred) -> float:
    score = 1.0
    for approach, value in configs['eval']['reference_answers'].items():
        match approach:
            case 'exact_match':
                score *= exact_match(ref=value, pred=pred)

            case 'must_include':
                assert isinstance(value, list)
                for must_value in value:
                    score *= must_include(
                        ref=must_value,
                        pred=pred,
                        tokenize=(len(value) == 1),
                    )
            case 'fuzzy_match':
                intent = configs['intent']
                if value == 'N/A':
                    # For N/A answers, skip the ua_match and use fuzzy_match directly
                    # This ensures we're using our improved Finish[] extraction logic
                    assert isinstance(configs['eval'].get('string_note', ''), str)
                    fuzzy_result = fuzzy_match(
                        ref=configs['eval'].get('string_note', 'Task is not achievable'), 
                        pred=pred, 
                        intent=intent
                    )
                    # Handle tuple return type
                    if isinstance(fuzzy_result, tuple):
                        fuzzy_score, fuzzy_reasoning = fuzzy_result
                        if fuzzy_reasoning:
                            logger.info(f"Fuzzy match reasoning for false result: {fuzzy_reasoning}")
                        score *= fuzzy_score
                    else:
                        # Backward compatibility if still returns float
                        score *= fuzzy_result
                else:
                    assert isinstance(value, list)
                    for reference in value:
                        fuzzy_result = fuzzy_match(
                            ref=reference, pred=pred, intent=intent
                        )
                        # Handle tuple return type
                        if isinstance(fuzzy_result, tuple):
                            fuzzy_score, fuzzy_reasoning = fuzzy_result
                            if fuzzy_reasoning:
                                logger.info(f"Fuzzy match reasoning for false result: {fuzzy_reasoning}")
                            score *= fuzzy_score
                        else:
                            # Backward compatibility if still returns float
                            score *= fuzzy_result
    return score

def parse_urls(history) -> List[str]:
    urls = []
    for line in history.split('\n'):
        # Handle browser-based agent format (case-insensitive)
        if line.lower().startswith('url: '):
            urls.append(line.split(': ', 1)[1])  # Use split with maxsplit=1 to handle URLs with colons
        # Handle API-based agent format
        elif 'call_function' in line:
            # Extract URL from call_function output
            url_match = re.search(r'url: (.*?)(?=\n|$)', line)
            if url_match:
                urls.append(url_match.group(1))
    return urls

def get_url(history, pred) -> str:
    urls = parse_urls(history)
    if len(urls) == 0: return ''
    return urls[-1]

def clean_url(url: str) -> str:
    url = str(url)
    if url.startswith('"') or url.startswith("'"):
        url = url.replace('"', '')
        url = url.replace("'", '')
    url = url.rstrip('/')
    return url

def parse_url(url: str) -> tuple[str, dict[str, list[str]]]:
    """Parse a URL into its base, path, and query components."""
    url = urllib.parse.unquote(url)
    parsed_url = urllib.parse.urlparse(url)
    base_path = parsed_url.netloc + parsed_url.path
    query = urllib.parse.parse_qs(parsed_url.query)
    return base_path, query

def parse_url_list(urls: list[str]) -> tuple[list[str], dict[str, set[str]]]:
    """Parse a list of URLs."""
    base_paths = []
    queries = collections.defaultdict(set)
    for url in urls:
        base_path, query = parse_url(url)
        base_paths.append(base_path)
        for k, v in query.items():
            queries[k].update(v)
    return base_paths, queries

def parse_parameter(param):
    """
    Normalize parameters from a URL string or a dictionary.
    Returns: dict[str, list[str]]
    """
    import urllib.parse
    import ast
    if isinstance(param, dict):
        # URL decode values in the dictionary
        result = {}
        for k, v in param.items():
            if isinstance(v, list):
                result[k] = [urllib.parse.unquote_plus(str(x)) for x in v]
            else:
                result[k] = [urllib.parse.unquote_plus(str(v))]
        return result
    elif isinstance(param, str):
        # Try to parse as dict if it looks like one
        try:
            parsed = ast.literal_eval(param)
            if isinstance(parsed, dict):
                result = {}
                for k, v in parsed.items():
                    if isinstance(v, list):
                        result[k] = [urllib.parse.unquote_plus(str(x)) for x in v]
                    else:
                        result[k] = [urllib.parse.unquote_plus(str(v))]
                return result
            if isinstance(parsed, list) and len(parsed) > 0 and isinstance(parsed[0], dict):
                # If it's a list of dicts, merge all keys
                merged = {}
                for d in parsed:
                    for k, v in d.items():
                        if k not in merged:
                            merged[k] = []
                        if isinstance(v, list):
                            merged[k].extend([urllib.parse.unquote_plus(str(x)) for x in v])
                        else:
                            merged[k].append(urllib.parse.unquote_plus(str(v)))
                return merged
        except Exception:
            pass
        # Otherwise, parse as query string
        parsed_url = urllib.parse.urlparse(param)
        parsed_params = urllib.parse.parse_qs(parsed_url.query)
        # URL decode all values
        result = {}
        for k, v_list in parsed_params.items():
            result[k] = [urllib.parse.unquote_plus(v) for v in v_list]
        return result
    else:
        return {}

def url_match(configs, pred, history, check_all_history=False, log_file=None):
    def create_simple_details(score, method='parameter_matching', extra_info=None):
        """Helper to create simple details for non-LLM evaluations"""
        details = {
            'evaluation_method': method,
            'check_all_history': check_all_history,
            'success': score > 0,
            'html_url_detected': False
        }
        if extra_info:
            details.update(extra_info)
        return score, details
    
    # Only run if 'url_match' is in eval_types
    if 'url_match' not in configs['eval'].get('eval_types', []):
        return create_simple_details(1.0, 'not_required')

    # Get the reference URLs
    ref_urls = configs['eval'].get('reference_url', '')
    if not ref_urls:
        return create_simple_details(1.0, 'no_reference_urls')

    ref_urls = ref_urls.split(' |OR| ')
    ref_urls = [clean_url(url) for url in ref_urls]
    matching_rule = configs['eval'].get('url_note', 'GOLD in PRED')

    # Debug: Print reference URLs for inspection
    logger.info(f"URL Match - Reference URLs: {ref_urls}")
    def queries_match(ref_params, pred_params):
        """Check if the reference query parameters are contained in the prediction parameters"""
        logger.info(f"URL Match - Comparing params: {ref_params} vs {pred_params}")
        
        # Special handling for GitLab label parameters
        # GitLab web UI uses label_name[] while API uses labels
        if 'label_name[]' in ref_params and 'labels' in pred_params:
            ref_labels = ref_params['label_name[]']
            pred_labels = pred_params['labels']
            
            logger.info(f"URL Match - Found GitLab label parameters: {ref_labels} vs {pred_labels}")
            
            # Check if all reference labels are in the prediction labels
            # For GitLab, labels in API can be comma-separated
            pred_label_set = set()
            for label_str in pred_labels:
                for label in label_str.split(','):
                    pred_label_set.add(label.strip().lower())
            
            ref_label_set = {label.strip().lower() for label in ref_labels}
            
            logger.info(f"URL Match - Comparing label sets: {ref_label_set} vs {pred_label_set}")
            
            # Check if all ref labels are found in pred labels
            if ref_label_set.issubset(pred_label_set):
                logger.info("URL Match - GitLab labels match successfully")
                return True
            else:
                missing_labels = ref_label_set - pred_label_set
                logger.info(f"URL Match - GitLab labels don't match - missing: {missing_labels}")
                return False
        
        # Simple value-based matching: collect all values from both ref and pred, then compare
        logger.info("URL Match - Using simple value-based matching (ignore key names)")
        
        # Collect all reference values
        ref_all_values = set()
        for ref_key, ref_values in ref_params.items():
            for value in ref_values:
                ref_all_values.add(str(value).lower())
        
        # Collect all prediction values  
        pred_all_values = set()
        for pred_key, pred_values in pred_params.items():
            for value in pred_values:
                pred_all_values.add(str(value).lower())
        
        logger.info(f"URL Match - Reference values: {ref_all_values}")
        logger.info(f"URL Match - Prediction values: {pred_all_values}")
        
        # Check if all ref values can be found in pred values
        if ref_all_values.issubset(pred_all_values):
            logger.info(f"URL Match - All reference values found in prediction: {ref_all_values} ⊆ {pred_all_values}")
            return True
        else:
            missing_values = ref_all_values - pred_all_values
            logger.info(f"URL Match - Missing values in prediction: {missing_values}")
            return False

    # First, try LLM evaluation for HTML URLs (indicating web page navigation)
    for ref_url in ref_urls:
        if '.html' in ref_url:
            logger.info(f"URL Match - HTML URL detected, using LLM to evaluate task completion")
            
          
            extracted_answer = None
            
            # Extract final answer from Finish[] tag if present (but don't require it)
            finish_idx = pred.rfind("Finish[")
            if finish_idx >= 0:
                end_idx = pred.find("]", finish_idx)
                if end_idx >= 0:
                    extracted_answer = pred[finish_idx+7:end_idx].strip()
                    logger.info(f"URL Match - Extracted final answer: '{extracted_answer}'")
            else:
                logger.info("URL Match - No Finish[] tag found, will evaluate based on agent behavior")
                
            # Extract URLs from history for the new prompt
            url_calls = []
            lines = history.split('\n')
            url_line_count = 0
            for line in lines:
                # Look for URL: or url: patterns (case insensitive)
                stripped_line = line.strip()
                if stripped_line.lower().startswith('url:'):
                    url_calls.append(stripped_line)
                    url_line_count += 1
            
            url_calls_str = '\n'.join(url_calls) if url_calls else "No URLs found in execution log"
            logger.info(f"URL Match - Found {url_line_count} URL lines in history, extracted {len(url_calls)} URLs")
            if url_calls:
                logger.info(f"URL Match - Sample extracted URLs: {url_calls_str[:300]}...")
            
            # Extract reasoning from logs using helper function (similar to html_match)
            try:
                # Import the helper function
                import sys
                import os
                sys.path.append('/Users/jianhaonan/Desktop/API-Based-Agent')
                from extract_log import extract_agent_info
                
                # Use helper function if log_file is available, otherwise fallback to history
                if log_file:
                    extracted_log = extract_agent_info(log_file, num_last_steps=18)
                    logger.info(f"URL Match - Used helper function to extract agent reasoning from {log_file}")
                    logger.info(f"URL Match - Extracted log content preview: {extracted_log[:300]}...")
                else:
                    # Fallback to using recent history when log_file not available
                    if isinstance(history, str):
                        extracted_log = history[-2000:] if len(history) > 2000 else history
                    else:
                        history_str = str(history) if history else ""
                        extracted_log = history_str[-2000:] if len(history_str) > 2000 else history_str
                    logger.info(f"URL Match - No log_file available, using {len(extracted_log)} characters from history")
                
            except Exception as e:
                logger.warning(f"URL Match - Failed to extract log with helper function: {e}")
                # Fallback to using final answer and recent history
                if isinstance(history, str):
                    extracted_log = history[-2000:] if len(history) > 2000 else history
                else:
                    extracted_log = str(history)[-2000:] if len(str(history)) > 2000 else str(history)
                
            # Use LLM to evaluate if the task was completed based on final answer and task intent
            try:
                client = openai.OpenAI(
                    api_key=os.environ.get('OPENAI_API_KEY', '')
                )
                
                task_intent = configs.get('intent', 'No task intent provided')
                
                # Use your new prompt format for HTML URLs
                prompt = f"""You are evaluating an API agent's performance on the task: {task_intent}

The reference implementation accesses {ref_url}, but this agent uses a different API ecosystem. Your goal is to determine if the agent's API calls accomplish the same functional objective, regardless of specific endpoints used.

**Evaluation Criteria:**
1. **Functional Alignment**: Do the API calls serve the same purpose as the reference URL?
2. **Parameter Relevance**: Are the parameters extracted from the query and used appropriately?
3. **Logical Sequence**: Do the API calls follow a reasonable order to accomplish the task?
4. **Error Handling**: Does the agent handle failures gracefully and attempt alternatives?

**Assessment Guidelines:**
- SUCCESS if the agent's API calls would reasonably accomplish the same goal as the reference URL
- SUCCESS if the agent uses equivalent but different endpoints (e.g., different weather APIs for weather queries)
- SUCCESS if the agent makes multiple related calls that collectively achieve the objective
- FAIL only if the API calls are clearly unrelated to the task or would not achieve the intended outcome
- Consider the agent's reasoning process from the logs, not just the final API calls

**Agent Execution:**

URLs accessed:
{url_calls_str}

Execution log:
{extracted_log}

**Your Assessment:**
REASON: [One sentence explaining whether the agent's approach would accomplish the same objective as the reference URL, considering functional equivalence rather than exact matching]
DECISION: [success/fail]
"""
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that evaluates task completion based on final answers."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0,
                    max_tokens=300
                )
                
                llm_response = response.choices[0].message.content.strip()
                logger.info(f"URL Match - LLM evaluation response: {llm_response}")
                
                # Parse LLM response in new format (handle markdown formatting)
                reason_match = re.search(r'(\*\*)?REASON:(\*\*)?\s*(.+)', llm_response, re.DOTALL)
                decision_match = re.search(r'(\*\*)?DECISION:(\*\*)?\s*(success|fail)', llm_response, re.IGNORECASE)
                
                llm_score = 0.0  # Default to fail if parsing fails
                llm_reasoning = "LLM evaluation failed to parse"
                
                if reason_match:
                    llm_reasoning = reason_match.group(3).strip()
                    # Clean up reasoning (remove any DECISION part that might be included)
                    if '**DECISION:**' in llm_reasoning:
                        llm_reasoning = llm_reasoning.split('**DECISION:**')[0].strip()
                    elif 'DECISION:' in llm_reasoning:
                        llm_reasoning = llm_reasoning.split('DECISION:')[0].strip()
                    
                if decision_match:
                    decision = decision_match.group(3).lower()
                    llm_score = 1.0 if decision == 'success' else 0.0
                
                # Create detailed results with LLM reasoning
                url_match_details = {
                    'evaluation_method': 'llm_evaluation',
                    'check_all_history': check_all_history,
                    'success': llm_score > 0,
                    'llm_prompt': prompt,
                    'llm_response': llm_response,
                    'llm_reasoning': llm_reasoning,
                    'extracted_answer': extracted_answer,
                    'task_intent': task_intent,
                    'html_url_detected': True,
                    'extracted_log_length': len(extracted_log)
                }
                
                if llm_score > 0:
                    logger.info("URL Match - LLM determined task was completed successfully")
                else:
                    logger.info("URL Match - LLM determined task was not completed successfully")
                
                return llm_score, url_match_details
                    
            except Exception as e:
                logger.error(f"URL Match - Error in LLM evaluation: {e}")
                error_details = {
                    'evaluation_method': 'llm_evaluation',
                    'check_all_history': check_all_history,
                    'success': False,
                    'error': str(e),
                    'html_url_detected': True
                }
                return 0.0, error_details

    # Unified evaluation logic - only difference is number of URLs examined
    # Get URLs to examine based on check_all_history flag
    if check_all_history:
        urls_to_examine = parse_urls(history)  # All URLs
        logger.info(f"URL Match - All History Mode: examining {len(urls_to_examine)} URLs")
    else:
        last_url = get_url(history, pred)  # Last URL only
        urls_to_examine = [last_url] if last_url else []
        logger.info(f"URL Match - Last Response Mode: examining {len(urls_to_examine)} URLs")
    
    # Extract parameters from URLs and parameter lines using identical logic
    all_params = []
    
    # Process URLs
    for url in urls_to_examine:
        if url:  # Skip empty URLs
            clean_url_val = clean_url(url)
            all_params.append(parse_parameter(clean_url_val))
            logger.info(f"URL Match - Found URL: {clean_url_val}")
    
    # Extract parameters from 'parameter:' lines (same for both modes)
    lines = history.split('\n')
    for line in lines:
        if line.strip().startswith('parameter:'):
            param_str = line.strip()[len('parameter:'):].strip()
            try:
                # Parse parameters in the format "key1=value1, key2=value2"
                param_dict = {}
                for pair in param_str.split(', '):
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        # URL decode the value to handle cases like 'usb+wifi' -> 'usb wifi'
                        param_dict[key] = [urllib.parse.unquote_plus(value)]
                all_params.append(param_dict)
                logger.info(f"URL Match - Found parameter line: {param_dict}")
            except Exception as e:
                logger.warning(f"URL Match - Error parsing parameter line: {e}")
    
    if not all_params:
        method_name = 'no_parameters_in_history' if check_all_history else 'no_parameters_found'
        logger.info(f"URL Match - No parameters found")
        return create_simple_details(0.0, method_name)
    
    # Check if any parameter set matches any reference URL (same logic for both modes)
    exact_match_found = False
    overlap_data = None
    
    for ref_url in ref_urls:
        ref_params = parse_parameter(ref_url)
        
        for params in all_params:
            # First try exact parameter matching
            if queries_match(ref_params, params):
                exact_match_found = True
                method_name = 'parameter_matching_all_history' if check_all_history else 'parameter_matching'
                logger.info(f"URL Match - Found exact matching parameters: {params}")
                return create_simple_details(1.0, method_name, {
                    'matched_params': params,
                    'ref_params': ref_params
                })
            
            # If exact match fails, check for overlap (for LLM evaluation)
            if not overlap_data:
                # Collect all reference parameter values
                ref_all_values = set()
                for ref_key, ref_values in ref_params.items():
                    for value in ref_values:
                        ref_all_values.add(str(value).lower())
                
                # Collect all prediction parameter values  
                pred_all_values = set()
                for pred_key, pred_values in params.items():
                    for value in pred_values:
                        pred_all_values.add(str(value).lower())
                
                # Check if there's any overlap
                overlap = ref_all_values.intersection(pred_all_values)
                if overlap:
                    overlap_data = {
                        'ref_values': list(ref_all_values),
                        'pred_values': list(pred_all_values),
                        'overlap': list(overlap),
                        'ref_params': ref_params,
                        'pred_params': params
                    }
                    logger.info(f"URL Match - Found parameter overlap: {overlap}")
    
    # If no exact match but there's overlap, use LLM evaluation
    if not exact_match_found and overlap_data:
        logger.info(f"URL Match - No exact match found, but overlap detected. Using LLM evaluation.")
        
        try:
            # Extract reasoning from logs using helper function
            try:
                import sys
                import os
                sys.path.append('/Users/jianhaonan/Desktop/API-Based-Agent')
                from extract_log import extract_agent_info
                
                # Use helper function if log_file is available, otherwise fallback to history
                if log_file:
                    extracted_log = extract_agent_info(log_file, num_last_steps=18)
                    logger.info(f"URL Match - Used helper function to extract agent reasoning from {log_file}")
                else:
                    # Fallback to using recent history when log_file not available
                    if isinstance(history, str):
                        extracted_log = history[-2000:] if len(history) > 2000 else history
                    else:
                        extracted_log = str(history)[-2000:] if len(str(history)) > 2000 else str(history)
                    logger.info(f"URL Match - No log_file available, using {len(extracted_log)} characters from history")
                
            except Exception as e:
                logger.warning(f"URL Match - Failed to extract log with helper function: {e}")
                extracted_log = str(history)[-1000:] if len(str(history)) > 1000 else str(history)
            
            task_intent = configs.get('intent', 'Complete the given task')
            
            # Build overlap description
            overlap_list = overlap_data['overlap']  # Already a list
            ref_set = set(overlap_data['ref_values'])
            pred_set = set(overlap_data['pred_values'])
            missing_list = list(ref_set - pred_set)
            
            overlap_str = f"Found parameters: {', '.join(overlap_list)}"
            if missing_list:
                overlap_str += f" | Missing parameters: {', '.join(missing_list)}"
            
            # Use the same template format for consistency
            ref_urls_str = ', '.join(configs.get('url', []))
            
            llm_prompt = f"""You are evaluating an API agent's performance on the task: {task_intent}

The reference implementation accesses {ref_urls_str}, but this agent uses a different API ecosystem. Your goal is to determine if the agent's API calls accomplish the same functional objective, regardless of specific endpoints used.

**Evaluation Criteria:**
1. **Functional Alignment**: Do the API calls serve the same purpose as the reference URL?
2. **Parameter Relevance**: Are the parameters extracted from the query and used appropriately?
3. **Logical Sequence**: Do the API calls follow a reasonable order to accomplish the task?
4. **Error Handling**: Does the agent handle failures gracefully and attempt alternatives?

**Assessment Guidelines:**
- SUCCESS if the agent's API calls would reasonably accomplish the same goal as the reference URL
- SUCCESS if the agent uses equivalent but different endpoints (e.g., different weather APIs for weather queries)  
- SUCCESS if the agent makes multiple related calls that collectively achieve the objective
- FAIL only if the API calls are clearly unrelated to the task or would not achieve the intended outcome
- Consider the agent's reasoning process from the logs, not just the final API calls

**Parameter Analysis:**
{overlap_str}
Required parameters: {', '.join(overlap_data['ref_values'])}
Agent parameters: {', '.join(overlap_data['pred_values'])}

**Agent Execution:**

Execution log:
{extracted_log}

**Your Assessment:**
REASON: [One sentence explaining whether the agent's approach would accomplish the same objective as the reference URL, considering functional equivalence rather than exact matching]
DECISION: [success/fail]
"""
            
            client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            llm_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": llm_prompt}],
                temperature=0
            )
            
            llm_content = llm_response.choices[0].message.content
            
            # Parse LLM response in new format (handle markdown formatting)
            reason_match = re.search(r'(\*\*)?REASON:(\*\*)?\s*(.+)', llm_content, re.DOTALL)
            decision_match = re.search(r'(\*\*)?DECISION:(\*\*)?\s*(success|fail)', llm_content, re.IGNORECASE)
            
            llm_score = 0.0  # Default to fail if parsing fails
            llm_reasoning = "LLM evaluation failed to parse"
            
            if reason_match:
                llm_reasoning = reason_match.group(3).strip()
                if '**DECISION:**' in llm_reasoning:
                    llm_reasoning = llm_reasoning.split('**DECISION:**')[0].strip()
                elif 'DECISION:' in llm_reasoning:
                    llm_reasoning = llm_reasoning.split('DECISION:')[0].strip()
                
            if decision_match:
                decision = decision_match.group(3).lower()
                llm_score = 1.0 if decision == 'success' else 0.0
            
            method_name = 'llm_overlap_evaluation_all_history' if check_all_history else 'llm_overlap_evaluation'
            
            details = {
                'evaluation_method': method_name,
                'check_all_history': check_all_history,
                'success': llm_score > 0,
                'html_url_detected': False,
                'overlap_found': True,
                'llm_prompt': llm_prompt,
                'llm_response': llm_content,
                'llm_reasoning': llm_reasoning,
                'overlap_data': overlap_data
            }
            
            logger.info(f"URL Match - LLM overlap evaluation score: {llm_score}")
            return llm_score, details
            
        except Exception as e:
            logger.error(f"URL Match - Error in LLM overlap evaluation: {e}")
            # Fall through to no match
    
    # No exact match and no overlap (or LLM evaluation failed)
    method_name = 'no_parameter_match_in_history' if check_all_history else 'no_parameter_match'
    logger.info("URL Match - No matching parameters found")
    return create_simple_details(0.0, method_name)

def html_match(task, response, log_file, history):
    """
    HTML evaluation function that always uses LLM for scoring.
    Text matching is only used to identify targets for LLM evaluation.
    
    Process:
    1. Extract task requirements and final answer
    2. Use text matching to identify relevant targets
    3. Always use LLM to evaluate if the task has been completed successfully
    
    Args:
        task: Task dictionary containing evaluation targets
        response: Agent response containing final answer
        log_file: Path to log file (can be None, will use history instead)
        history: Execution history data
        
    Returns:
        tuple: (html_score, html_details) where html_score is float and html_details is dict
    """
    # Extract targets from task and convert to proper format
    program_html_configs = task.get('eval', {}).get('program_html', [])
    targets = []
    
    for config in program_html_configs:
        required_contents = config.get('required_contents', {})
        
        # Handle must_include requirements
        must_include = required_contents.get('must_include', [])
        if isinstance(must_include, list):
            for must_include_item in must_include:
                targets.append({
                    'verification_type': 'must_include',
                    'value': must_include_item
                })
        elif must_include:  # Handle single string case
            targets.append({
                'verification_type': 'must_include',
                'value': must_include
            })
        
        # Handle exact_match requirements
        exact_match = required_contents.get('exact_match', [])
        if isinstance(exact_match, list):
            for exact_match_item in exact_match:
                targets.append({
                    'verification_type': 'exact_match', 
                    'value': exact_match_item
                })
        elif exact_match:  # Handle single string case (like task 448)
            targets.append({
                'verification_type': 'exact_match',
                'value': exact_match
            })
    
    logger.info(f"HTML Match - Starting evaluation for {len(targets)} targets")
    
    try:
        # Use history data instead of log file if log_file is None
        if log_file is None:
            # Convert history to string content for processing
            if isinstance(history, list):
                log_content = '\n'.join([str(item) for item in history])
            else:
                log_content = str(history) if history else ""
        else:
            # Read log file
            with open(log_file, 'r', encoding='utf-8') as f:
                log_content = f.read()
        
        # Skip initial task description lines before execution starts
        execution_start_patterns = [
            r'Step \d+:',
            r'act - \*\*',
            r'CONTENT: Think step by step',
            r'CODE:',
            r'obs - \*\*'
        ]
        
        log_lines = log_content.split('\n')
        execution_start_idx = 0
        
        for i, line in enumerate(log_lines):
            if any(re.search(pattern, line) for pattern in execution_start_patterns):
                execution_start_idx = i
                break
        
        # Extract execution history (skip task description)
        execution_content = '\n'.join(log_lines[execution_start_idx:])
        logger.info(f"HTML Match - Skipped {execution_start_idx} initial task description lines")
        
        # Extract API responses from execution history using case-insensitive patterns
        api_response_pattern = re.compile(r'CONTENT:\s*(.*?)(?=\nobs|\nStep|\Z)', re.IGNORECASE | re.DOTALL)
        content_pattern = re.compile(r'content:\s*(.*?)(?=\nobs|\nStep|\Z)', re.IGNORECASE | re.DOTALL)
        
        api_responses = []
        
        # Try both uppercase and lowercase patterns
        for pattern in [api_response_pattern, content_pattern]:
            matches = pattern.findall(execution_content)
            api_responses.extend([match.strip() for match in matches if match.strip()])
        
        combined_api_content = '\n'.join(api_responses)
        logger.info(f"HTML Match - Extracted {len(api_responses)} API response sections")
        
        # Extract final answer from Finish[] tag
        finish_pattern = re.compile(r'Finish\[(.*?)\]', re.IGNORECASE | re.DOTALL)
        finish_matches = finish_pattern.findall(response)
        final_answer = finish_matches[-1].strip() if finish_matches else ""
        
        logger.info(f"HTML Match - Extracted final answer: {final_answer[:100]}...")
        
        # Perform text matching to identify relevant targets
        target_results = []
        targets_passed_text_matching = []
        search_content = combined_api_content + '\n' + final_answer
        text_matching_used = True  # Flag to indicate if text matching was used
        
        for i, target in enumerate(targets):
            verification_type = target.get('verification_type', '')
            target_value = target.get('value', '')
            
            logger.info(f"HTML Match - Evaluating target {i}: {verification_type} = '{target_value}'")
            
            target_result = {
                'target_index': i,
                'verification_type': verification_type,
                'target_value': target_value,
                'score': 0.0,
                'success': False,
                'text_match_result': False,  # Track text matching result separately
                'evaluation_method': 'pending_llm'  # Will be updated after LLM evaluation
            }
            
            # Direct text matching for exact_match and must_include
            if verification_type in ['exact_match', 'must_include']:
                if verification_type == 'exact_match':
                    # Case-sensitive exact match
                    if target_value in search_content:
                        target_result['text_match_result'] = True
                        targets_passed_text_matching.append(i)
                        logger.info(f"HTML Match - Target {i}: Exact match found in text")
                    else:
                        logger.info(f"HTML Match - Target {i}: Exact match not found in text")
                
                elif verification_type == 'must_include':
                    # Case-insensitive inclusion check
                    if target_value.lower() in search_content.lower():
                        target_result['text_match_result'] = True
                        targets_passed_text_matching.append(i)
                        logger.info(f"HTML Match - Target {i}: Must include found in text")
                    else:
                        logger.info(f"HTML Match - Target {i}: Must include not found in text")
            else:
                # For other verification types, mark as unsupported
                logger.warning(f"HTML Match - Target {i}: Unsupported verification type '{verification_type}'")
                target_result['evaluation_method'] = 'unsupported'
            
            target_results.append(target_result)
        
        # Always use LLM for evaluation, even if no text matches were found
        # This ensures we rely on LLM judgment rather than text matching
        task_intent = task.get('intent', 'Complete the given task')
        
        # Build list of all requirements for LLM evaluation
        requirements_list = []
        for i, target in enumerate(targets):
            requirements_list.append(f"{target['verification_type']}: '{target['value']}'")
        
        evaluator_str = ', '.join(requirements_list)
        
        # Extract reasoning from logs using helper function
        try:
            # Import the helper function
            import sys
            import os
            sys.path.append('/Users/jianhaonan/Desktop/API-Based-Agent')
            from extract_log import extract_agent_info
            
            # Extract last 5 steps of agent reasoning
            if log_file:
                extracted_log = extract_agent_info(log_file, num_last_steps=18)
                logger.info(f"HTML Match - Extracted log from file for LLM evaluation")
            else:
                # Fallback: use the history content if no log file
                extracted_log = history[-2000:] if len(history) > 2000 else history
            
            logger.info(f"HTML Match - Extracted {len(extracted_log)} characters from log for LLM evaluation")
            
        except Exception as e:
            logger.warning(f"HTML Match - Failed to extract log with helper function: {e}")
            # Fallback to using execution content
            extracted_log = execution_content[-2000:] if len(execution_content) > 2000 else execution_content
        
        
        llm_prompt = f"""You are evaluating an agent's performance on the task: {task_intent}

Below are the truncated execution logs. Determine whether the agent has successfully completed the task based on the requirements.
{extracted_log}

IMPORTANT: Your evaluation should be based on whether the agent achieved the task's objective, not just on exact text matches.
Focus on the logical reasoning path and the final outcome.

AGENT'S FINAL ANSWER: {final_answer}

Provide your assessment in this exact format:
REASON: [One sentence explaining your decision]
DECISION: [success/fail]


"""
        
        try:
            client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            llm_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": llm_prompt}],
                temperature=0
            )
            
            llm_content = llm_response.choices[0].message.content
            
            # Parse LLM response in new format (handle both markdown and plain text)
            reason_match = re.search(r'(\*\*)?REASON:(\*\*)?\s*(.+)', llm_content, re.DOTALL)
            decision_match = re.search(r'(\*\*)?DECISION:(\*\*)?\s*(success|fail)', llm_content, re.IGNORECASE)
            
            llm_score = 0.0  # Default to fail if parsing fails
            llm_reasoning = "LLM evaluation failed to parse"
            
            if reason_match:
                llm_reasoning = reason_match.group(3).strip()
                # Clean up reasoning (remove any DECISION part that might be included)
                if '**DECISION:**' in llm_reasoning:
                    llm_reasoning = llm_reasoning.split('**DECISION:**')[0].strip()
                elif 'DECISION:' in llm_reasoning:
                    llm_reasoning = llm_reasoning.split('DECISION:')[0].strip()
                
            if decision_match:
                decision = decision_match.group(3).lower()
                llm_score = 1.0 if decision == 'success' else 0.0
            
            # Apply LLM result to all targets
            for i in range(len(target_results)):
                target_results[i]['llm_response'] = llm_content
                target_results[i]['llm_prompt'] = llm_prompt
                target_results[i]['llm_reasoning'] = llm_reasoning
                target_results[i]['evaluation_method'] = 'llm_evaluation'
                target_results[i]['score'] = llm_score  # Use LLM score for all targets
                target_results[i]['success'] = llm_score >= 0.5
            
            logger.info(f"HTML Match - LLM evaluation completed with score = {llm_score}")
            
            # Create detailed results for return
            html_details = {
                'target_evaluations': target_results,
                'overall_success': llm_score >= 0.5,
                'total_targets': len(targets),
                'text_matching_used': text_matching_used,
                'text_matching_results': {
                    'targets_passed': len(targets_passed_text_matching),
                    'targets_failed': len(targets) - len(targets_passed_text_matching),
                    'passed_indices': targets_passed_text_matching
                },
                'llm_evaluation': {
                    'score': llm_score,
                    'reasoning': llm_reasoning,
                    'decision': 'success' if llm_score >= 0.5 else 'fail'
                }
            }
            
            logger.info(f"HTML Match - Overall evaluation complete: {llm_score}")
            
            return llm_score, html_details
            
        except Exception as e:
            logger.error(f"HTML Match - LLM evaluation failed: {e}")
            error_details = {
                'target_evaluations': target_results,
                'overall_success': False,
                'total_targets': len(targets),
                'text_matching_used': text_matching_used,
                'text_matching_results': {
                    'targets_passed': len(targets_passed_text_matching),
                    'targets_failed': len(targets) - len(targets_passed_text_matching)
                },
                'error': str(e)
            }
            return 0.0, error_details
        
    except Exception as e:
        logger.error(f"HTML Match - Evaluation failed: {e}")
        error_details = {
            'target_evaluations': [],
            'overall_success': False,
            'total_targets': len(targets),
            'text_matching_used': False,
            'error': str(e)
        }
        return 0.0, error_details

def check_correctness(task, response, log_file, check_all_history=False):
    # Check if this is a glycan task first
    if task.get('sites') == ['glycan'] or 'glycan_gpt_evaluation' in task.get('eval', {}).get('eval_types', []):
        try:
            from glycan_evaluation import check_correctness_glycan
            return check_correctness_glycan(task, response, log_file, check_all_history)
        except ImportError as e:
            logger.error(f"Could not import glycan evaluation: {e}")
            return False, {'error': f'Could not import glycan evaluation: {e}'}
    
    # Original WebArena evaluation logic for non-glycan tasks
    score = 1.0
    evaluation_details = {
        'eval_types': task['eval']['eval_types'],
        'string_match_score': None,
        'string_match_details': None,
        'url_match_score': None,
        'url_match_details': None,
        'html_match_score': None,
        'html_match_details': None,
        'overall_score': 0.0,
        'overall_success': False,
        'evaluation_breakdown': []
    }
    
    # string match
    if 'string_match' in task['eval']['eval_types']:
        string_match_score = string_match(task, response)
        original_response = response
        if (string_match_score != 1.0):
            response = response.replace('"', '')
            response = response.replace("'", '')
            response = response.replace(' ', '')
            string_match_score = string_match(task, response)
        
        evaluation_details['string_match_score'] = string_match_score
        evaluation_details['string_match_details'] = {
            'original_response': original_response,
            'processed_response': response,
            'success': string_match_score > 0
        }
        evaluation_details['evaluation_breakdown'].append({
            'type': 'string_match',
            'score': string_match_score,
            'success': string_match_score > 0
        })
        score *= string_match_score
    
    # url match
    with open(log_file, 'r') as f: 
        history = f.read()
    
    if 'url_match' in task['eval']['eval_types']: 
        url_match_result = url_match(task, response, history, check_all_history=check_all_history, log_file=log_file)
        
        # Handle both old format (float) and new format (tuple)
        if isinstance(url_match_result, tuple):
            url_match_score, url_match_details = url_match_result
        else:
            url_match_score = url_match_result
            url_match_details = {
                'check_all_history': check_all_history,
                'success': url_match_score > 0
            }
        
        evaluation_details['url_match_score'] = url_match_score
        evaluation_details['url_match_details'] = url_match_details
        evaluation_details['evaluation_breakdown'].append({
            'type': 'url_match',
            'score': url_match_score,
            'success': url_match_score > 0
        })
        score *= url_match_score
    
    if score != 1.0: 
        evaluation_details['overall_score'] = score
        evaluation_details['overall_success'] = False
        return False, evaluation_details
    
    # If program_html evaluation is needed, use our new LLM-based html_match
    if 'program_html' in task['eval']['eval_types']: 
        html_score, html_details = html_match(task, response, None, history)
        evaluation_details['html_match_score'] = html_score
        evaluation_details['html_match_details'] = html_details
        evaluation_details['evaluation_breakdown'].append({
            'type': 'html_match',
            'score': html_score,
            'success': html_score > 0,
            'llm_evaluations': html_details
        })
        score *= html_score
    
    evaluation_details['overall_score'] = score
    evaluation_details['overall_success'] = score == 1.0
    
    return score == 1.0, evaluation_details