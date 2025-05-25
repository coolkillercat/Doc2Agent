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
os.environ['OPENAI_API_KEY'] = ""

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
    json_file_path = '/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/test.raw.json'
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
    api_file_path = '/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api/shopping/shopping.txt'
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
    api_file_path = '/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api/map/map.txt'
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

def get_initial_prompt_from_task(task):
    sites = task['sites']
    if sites == ['gitlab'] or ('gitlab' in sites and 'wikipedia' in sites): 
        site_name = 'gitlab'
        site_base = os.getenv('GITLAB')
        os.environ['GITLAB_START_URL'] = task['start_url']
        logger.info(f"os.environ['GITLAB_START_URL']: {os.environ['GITLAB_START_URL']}")
        return get_initial_prompt(site_name, site_base, task, get_gitlab_apis(), gitlab_token)
    if sites == ['shopping']: 
        site_name = 'shopping'
        site_base = os.getenv('SHOPPING')
        shopping_api_file = get_shopping_apis()
        os.environ['SHOPPING_START_URL'] = task['start_url']
        logger.info(f"os.environ['SHOPPING_START_URL']: {os.environ['SHOPPING_START_URL']}")
        admin_token = get_shopping_admin_auth_token()
        customer_token = get_shopping_customer_auth_token()
        extra_user_info = f'You should always use my access token {admin_token} in general. However, only when using the endpoints that contains `/V1/carts/mine` in the API, you must use this access token: {customer_token}, which you must not use for any other endpoints. For example, for the API endpoint `V1/products` you should use {admin_token}; while for the `/V1/carts/mine/items` endpoint, you should use {customer_token}.\n'
        return get_initial_prompt(site_name, site_base, task, shopping_api_file, '', extra_user_info)
    if sites == ['shopping_admin']:
        site_name = 'shopping_admin'
        site_base = os.getenv('SHOPPING_ADMIN')
        shopping_api_file = get_shopping_apis()
        os.environ['SHOPPING_ADMIN_START_URL'] = task['start_url']
        logger.info(f"os.environ['SHOPPING_ADMIN_START_URL']: {os.environ['SHOPPING_ADMIN_START_URL']}")
        admin_token = get_shopping_admin_admin_auth_token()
        return get_initial_prompt(site_name, site_base, task, shopping_api_file, admin_token, '')
    if sites == ['map'] or ('map' in sites and 'wikipedia' in sites):
        site_name = 'map'
        site_base = os.getenv('MAP')
        map_api_file = get_map_apis()
        os.environ['MAP_START_URL'] = task['start_url']
        logger.info(f"os.environ['MAP_START_URL']: {os.environ['MAP_START_URL']}")
        return get_initial_prompt(site_name, site_base, task, map_api_file, '', '')
    if sites == ['reddit']:
        site_name = 'reddit'
        site_base = os.getenv('REDDIT')
        reddit_api_file = get_reddit_apis()
        os.environ['REDDIT_START_URL'] = task['start_url']
        logger.info(f"os.environ['REDDIT_START_URL']: {os.environ['REDDIT_START_URL']}")
        return get_initial_prompt(site_name, site_base, task, reddit_api_file, '', '')
    if sites == ['map', 'shopping_admin']:
        shopping_admin_site = {'site_base': os.getenv('SHOPPING_ADMIN'), 'api_info': get_shopping_apis(), 'api_token': get_shopping_admin_admin_auth_token(), 'extra_user_info': ''}
        map_site = {'site_base': os.getenv('MAP'), 'api_info': get_map_apis(), 'api_token': '', 'extra_user_info': ''}
        sites = {'shopping_admin': shopping_admin_site, 'map': map_site}
        return get_initial_prompt_multi(sites, task)
    if sites == ['shopping', 'reddit']:
        shopping_site = {'site_base': os.getenv('SHOPPING'), 'api_info': get_shopping_apis(), 'api_token': get_shopping_admin_auth_token(), 'extra_user_info': ''}
        reddit_site = {'site_base': os.getenv('REDDIT'), 'api_info': get_reddit_apis(), 'api_token': '', 'extra_user_info': ''}
        sites = {'shopping': shopping_site, 'reddit': reddit_site}
        return get_initial_prompt_multi(sites, task)
    if sites == ['gitlab', 'reddit'] or sites == ['reddit', 'gitlab']:
        gitlab_site = {'site_base': os.getenv('GITLAB'), 'api_info': get_gitlab_apis(), 'api_token': gitlab_token, 'extra_user_info': ''}
        reddit_site = {'site_base': os.getenv('REDDIT'), 'api_info': get_reddit_apis(), 'api_token': '', 'extra_user_info': ''}
        sites = {'gitlab': gitlab_site, 'reddit': reddit_site}
        return get_initial_prompt_multi(sites, task)
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
    clean_ref = clean_answer(ref)
    clean_pred = clean_answer(pred)
    return float(clean_ref in clean_pred)

def fuzzy_match(ref, pred, intent, max_len=2000, retries=2):
    # Truncate to avoid context length errors
    ref = ref[:max_len]
    pred = pred[:max_len]
    for attempt in range(retries):
        try:
            return llm_fuzzy_match(pred, ref, intent)
        except openai.error.RateLimitError:
            print(f"Rate limit hit, waiting and retrying... (attempt {attempt+1})")
            time.sleep(1)
        except openai.error.APIConnectionError:
            print(f"Connection error, waiting and retrying... (attempt {attempt+1})")
            time.sleep(1)
        except openai.error.InvalidRequestError as e:
            if "context length" in str(e):
                print("Context length exceeded, waiting and skipping this instance.")
                time.sleep(1)
                return 0.0
            else:
                raise
        except Exception as e:
            print(f"Other error: {e}")
            return 0.0
    print("Max retries exceeded, skipping this instance.")
    return 0.0

def ua_match(ref: str, pred: str, intent: str) -> float:
    return llm_ua_match(pred, ref, intent)

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
                    # if the instruction only asks the model to generate N/A when encountering an unachievable task
                    # without more concrete reasons
                    score *= exact_match(ref=value, pred=pred)
                    # if the instruction also asks the model to generate the reason why the task is unachievable
                    # this should be the default as it will prevent false positive N/A`
                    if score != 1:
                        score = 1.0 * ua_match(
                            intent=configs['intent'],
                            ref=configs['eval']['string_note'],
                            pred=pred,
                        )
                else:
                    assert isinstance(value, list)
                    for reference in value:
                        score *= fuzzy_match(
                            ref=reference, pred=pred, intent=intent
                        )
    return score

def parse_urls(history) -> List[str]:
    urls = []
    for line in history.split('\n'):
        # Handle browser-based agent format
        if line.startswith('url: '):
            urls.append(line.split('url: ')[1])
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

def parse_urls(urls: list[str]) -> tuple[list[str], dict[str, set[str]]]:
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
    if isinstance(param, dict):
        return {k: [str(v)] if not isinstance(v, list) else [str(x) for x in v] for k, v in param.items()}
    elif isinstance(param, str):
        parsed_url = urllib.parse.urlparse(param)
        return urllib.parse.parse_qs(parsed_url.query)
    else:
        return {}

def url_match(configs, pred, history, check_all_history=False) -> float:
    # Only run if 'url_match' is in eval_types
    if 'url_match' not in configs['eval'].get('eval_types', []):
        return 1.0

    # Get the reference URLs
    ref_urls = configs['eval'].get('reference_url', '')
    if not ref_urls:
        return 1.0

    ref_urls = ref_urls.split(' |OR| ')
    ref_urls = [clean_url(url) for url in ref_urls]
    matching_rule = configs['eval'].get('url_note', 'GOLD in PRED')

    def queries_match(q1, q2):
        # Only require that all keys in q1 are present in q2 (q2 can have extra keys)
        if not set(q1.keys()).issubset(set(q2.keys())):
            return False
        for k in q1:
            if sorted(q1[k]) != sorted(q2[k]):
                return False
        return True

    def parse_parameter(param):
        import urllib.parse
        import ast
        if isinstance(param, dict):
            return {k: [str(v)] if not isinstance(v, list) else [str(x) for x in v] for k, v in param.items()}
        elif isinstance(param, str):
            # Try to parse as dict if it looks like one
            try:
                parsed = ast.literal_eval(param)
                if isinstance(parsed, dict):
                    return {k: [str(v)] if not isinstance(v, list) else [str(x) for x in v] for k, v in parsed.items()}
                if isinstance(parsed, list) and len(parsed) > 0 and isinstance(parsed[0], dict):
                    # If it's a list of dicts, merge all keys
                    merged = {}
                    for d in parsed:
                        for k, v in d.items():
                            if k not in merged:
                                merged[k] = []
                            if isinstance(v, list):
                                merged[k].extend([str(x) for x in v])
                            else:
                                merged[k].append(str(v))
                    return merged
            except Exception:
                pass
            # Otherwise, parse as query string
            parsed_url = urllib.parse.urlparse(param)
            return urllib.parse.parse_qs(parsed_url.query)
        else:
            return {}

    if check_all_history:
        all_urls = []
        all_params = []
        lines = history.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith('url: '):
                url = line.split('url: ')[1].strip()
                all_urls.append(clean_url(url))
                # Look ahead for parameter or content
                param_dict = None
                for j in range(1, 4):  # look up to 3 lines ahead
                    if i + j < len(lines):
                        next_line = lines[i + j].strip()
                        if next_line.startswith('parameter:'):
                            param_str = next_line[len('parameter:'):].strip()
                            param_dict = parse_parameter(param_str)
                            break
                        elif next_line.startswith('content:'):
                            content_str = next_line[len('content:'):].strip()
                            param_dict = parse_parameter(content_str)
                            break
                if param_dict is None:
                    param_dict = parse_parameter(url)  # fallback to query string
                all_params.append(param_dict)
            elif 'call_function' in line:
                url_match = re.search(r'url: (.*?)(?=\n|$)', line)
                if url_match:
                    url = url_match.group(1).strip()
                    all_urls.append(clean_url(url))
                    # Look ahead for parameter or content
                    param_dict = None
                    for j in range(1, 4):
                        if i + j < len(lines):
                            next_line = lines[i + j].strip()
                            if next_line.startswith('parameter:'):
                                param_str = next_line[len('parameter:'):].strip()
                                param_dict = parse_parameter(param_str)
                                break
                            elif next_line.startswith('content:'):
                                content_str = next_line[len('content:'):].strip()
                                param_dict = parse_parameter(content_str)
                                break
                    if param_dict is None:
                        param_dict = parse_parameter(url)
                    all_params.append(param_dict)
            i += 1
        last_url = get_url(history, pred)
        if last_url:
            all_urls.append(clean_url(last_url))
            all_params.append(parse_parameter(last_url))
        if not all_urls:
            return 0.0
        for ref_url in ref_urls:
            ref_base_path = ''
            if isinstance(ref_url, str):
                parsed_url = urllib.parse.urlparse(ref_url)
                ref_base_path = parsed_url.netloc + parsed_url.path
            ref_query = parse_parameter(ref_url)
            for url, param in zip(all_urls, all_params):
                pred_base_path = ''
                if isinstance(url, str):
                    parsed_url = urllib.parse.urlparse(url)
                    pred_base_path = parsed_url.netloc + parsed_url.path
                pred_query = param
                if matching_rule == 'GOLD in PRED':
                    if ref_base_path in pred_base_path and queries_match(ref_query, pred_query):
                        return 1.0
                elif matching_rule == 'PRED in GOLD':
                    if pred_base_path in ref_base_path and queries_match(ref_query, pred_query):
                        return 1.0
                else:  # exact match
                    if ref_url == url:
                        return 1.0
        return 0.0
    else:
        last_url = get_url(history, pred)
        last_url = clean_url(last_url)
        if last_url == '':
            return 0.0
        ref_base_path = ''
        if isinstance(ref_urls[0], str):
            parsed_url = urllib.parse.urlparse(ref_urls[0])
            ref_base_path = parsed_url.netloc + parsed_url.path
        ref_query = parse_parameter(ref_urls[0])
        pred_base_path = ''
        if isinstance(last_url, str):
            parsed_url = urllib.parse.urlparse(last_url)
            pred_base_path = parsed_url.netloc + parsed_url.path
        pred_query = parse_parameter(last_url)
        if matching_rule == 'GOLD in PRED':
            return 1.0 if ref_base_path in pred_base_path and queries_match(ref_query, pred_query) else 0.0
        elif matching_rule == 'PRED in GOLD':
            return 1.0 if pred_base_path in ref_base_path and queries_match(ref_query, pred_query) else 0.0
        else:  # exact match
            return 1.0 if last_url in ref_urls else 0.0

def program_html(configs, config_file, pred, page, history) -> float:
    targets = configs['eval']['program_html']
    score = 1.0
    for target in targets:
        target_url: str = target['url']  # which url to check
        if target_url.startswith('func'):
            func = target_url.split('func:')[1]
            last_url = get_url(history, pred)
            last_url = clean_url(last_url)
            if last_url == '': 
                # For API-based agents, try to get content from API responses
                api_response_match = re.search(r'content: (.*?)(?=\n\n|\Z)', history, re.DOTALL)
                if api_response_match:
                    selected_element = api_response_match.group(1)
                    selected_element = html.unescape(selected_element)
                    
                    if 'exact_match' in target['required_contents']:
                        required_contents = target['required_contents']['exact_match']
                        cur_score = exact_match(ref=required_contents, pred=selected_element)
                        score *= float(cur_score)
                    elif 'must_include' in target['required_contents']:
                        required_contents = target['required_contents']['must_include']
                        assert isinstance(required_contents, list)
                        for content in required_contents:
                            content_or = content.split(' |OR| ')
                            cur_score = any([must_include(ref=content, pred=selected_element, tokenize=False) 
                                          for content in content_or])
                            score *= float(cur_score)
                    continue
                return 0.0
            
            page.goto(last_url)
            time.sleep(3)
            func = func.replace('__last_url__', page.url)
            target_url = eval(func)
            
        locator: str = target['locator']  # js element locator
        if target_url != 'last':
            page.goto(target_url)
            time.sleep(3)
        else:
            last_url = get_url(history, pred)
            last_url = clean_url(last_url)
            if last_url == '':
                # For API-based agents, try to get content from API responses
                api_response_match = re.search(r'content: (.*?)(?=\n\n|\Z)', history, re.DOTALL)
                if api_response_match:
                    selected_element = api_response_match.group(1)
                    selected_element = html.unescape(selected_element)
                    
                    if 'exact_match' in target['required_contents']:
                        required_contents = target['required_contents']['exact_match']
                        cur_score = exact_match(ref=required_contents, pred=selected_element)
                        score *= float(cur_score)
                    elif 'must_include' in target['required_contents']:
                        required_contents = target['required_contents']['must_include']
                        assert isinstance(required_contents, list)
                        for content in required_contents:
                            content_or = content.split(' |OR| ')
                            cur_score = any([must_include(ref=content, pred=selected_element, tokenize=False) 
                                          for content in content_or])
                            score *= float(cur_score)
                    continue
                return 0.0
                
            page.goto(last_url)
            time.sleep(3)
            
        try:
            if not locator.strip():
                selected_element = page.content()
            elif locator.startswith('document.') or locator.startswith('[...document.'):
                if 'prep_actions' in target:
                    try:
                        for prep_action in target['prep_actions']:
                            page.evaluate(f'() => {prep_action}')
                    except Exception:
                        pass
                try:
                    selected_element = str(page.evaluate(f'() => {locator}'))
                    if not selected_element: selected_element = ''
                except Exception:
                    # the page is wrong, return empty
                    selected_element = ''
            elif locator.startswith('func:'):  # a helper function
                func = locator.split('func:')[1]
                func = func.replace('__page__', 'page')
                selected_element = eval(func)
            else: raise ValueError(f'Unknown locator: {locator}')
        except Exception as e:
            logger.info(f'exception in program_html: {e}')
            selected_element = ''
        selected_element = html.unescape(selected_element)
        if 'exact_match' in target['required_contents']:
            required_contents = target['required_contents']['exact_match']
            cur_score = exact_match(
                ref=required_contents, pred=selected_element
            )
            score *= float(cur_score)
        elif 'must_include' in target['required_contents']:
            required_contents = target['required_contents']['must_include']
            assert isinstance(required_contents, list)
            for content in required_contents:
                content_or = content.split(' |OR| ')
                cur_score = any(
                    [
                        must_include(
                            ref=content,
                            pred=selected_element,
                            tokenize=False,
                        )
                        for content in content_or
                    ]
                )
                score *= float(cur_score)
        else:
            raise ValueError(
                f"Unknown required_contents: {target['required_contents'].keys()}"
            )
    return score

def html_match(configs, pred, page, history) -> float:
    temp_dir = tempfile.mkdtemp()
    config_file = f"{temp_dir}/{configs['task_id']}.json"
    with open(config_file, 'w') as f:
        json.dump(configs, f)
    score = program_html(configs, config_file, pred, page, history)
    return score

def check_correctness(task, response, log_file, check_all_history=False):
    # use the answer if the task requires string_match + exact_match;
    # use the response (the final message from the agent) if the task requires string_match but not exact_match
    # do not use response nor answer if the task requires program_html match or url_match
    score = 1.0
    # string match
    if 'string_match' in task['eval']['eval_types']:
        string_match_score = string_match(task, response)
        if (string_match_score != 1.0):
            response = response.replace('"', '')
            response = response.replace("'", '')
            response = response.replace(' ', '')
            string_match_score = string_match(task, response)
        score *= string_match_score
    # url match
    with open(log_file, 'r') as f: history = f.read()
    if 'url_match' in task['eval']['eval_types']: 
        score *= url_match(task, response, history, check_all_history=check_all_history)
    if score != 1.0: return False
    if 'program_html' not in task['eval']['eval_types']: return score == 1.0
    # setup context manager
    context_manager = sync_playwright()
    playwright = context_manager.__enter__()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    sites = task['sites']
    if 'gitlab' in sites:
        username = 'byteblaze'
        password = 'hello1234'
        GITLAB_URL = os.environ['GITLAB']
        page.goto(f'{GITLAB_URL}/users/sign_in')
        page.get_by_test_id('username-field').click()
        page.get_by_test_id('username-field').fill(username)
        page.get_by_test_id('username-field').press('Tab')
        page.get_by_test_id('password-field').fill(password)
        page.get_by_test_id('sign-in-button').click()
        context.storage_state(path='/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/.auth/gitlab_state.json')
    if 'shopping' in sites:
        username = 'emma.lopez@gmail.com'
        password = 'Password.123'
        SHOPPING = os.environ['SHOPPING']
        logger.info(f"[DEBUG] Navigating to shopping login page: {SHOPPING}/customer/account/login/")
        page.goto(f'{SHOPPING}/customer/account/login/', timeout=10000)
        logger.info("[DEBUG] Filling email field...")
        page.get_by_label('Email', exact=True, timeout=10000).fill(username)
        logger.info("[DEBUG] Filling password field...")
        page.get_by_label('Password', exact=True, timeout=10000).fill(password)
        logger.info("[DEBUG] Clicking Sign In button...")
        page.get_by_role('button', name='Sign In', timeout=10000).click()
        logger.info("[DEBUG] Finished shopping login steps.")
        context.storage_state(path='/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/.auth/shopping_state.json')
    if 'shopping_admin' in sites:
        username = 'admin'
        password = 'admin1234'
        SHOPPING_ADMIN = os.environ['SHOPPING_ADMIN']
        page.goto(f'{SHOPPING_ADMIN}')
        page.get_by_label('Username', exact=True).fill(username)
        page.get_by_label('Password', exact=True).fill(password)
        page.get_by_role('button', name='Sign in').click()
        context.storage_state(path='/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/.auth/shopping_admin_state.json')
    if 'reddit' in sites:
        username = 'MarvelsGrantMan136'
        password = 'test1234'
        REDDIT = os.environ['REDDIT']
        page.goto(f'{REDDIT}/login')
        page.get_by_label('Username').fill(username)
        page.get_by_label('Password').fill(password)
        page.get_by_role('button', name='Log in').click()
        context.storage_state(path='/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/.auth/reddit_state.json')
    if 'program_html' in task['eval']['eval_types']: score *= html_match(task, response, page, history)
    context_manager.__exit__()
    return score == 1.0