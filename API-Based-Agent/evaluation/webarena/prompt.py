import requests
from bs4 import BeautifulSoup
import json
import os
from os import path
import sys


def get_tools_list_for_prompt(site='shopping', subdirectory=None):
    """
    Gets available tools for inclusion in prompts.
    Returns a formatted string listing all available tools and their descriptions.
    """
    try:
        # Special handling for GitLab with subdirectory
        if site == 'gitlab' and subdirectory:
            # Look for the tool_description.json file in the specified subdirectory
            descriptions_paths = [
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/api', site, 'tools', subdirectory, 'tool_description.json'),
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/workspace/api', site, 'tools', subdirectory, 'tool_description.json'),
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api', site, 'tools', subdirectory, 'tool_description.json')
            ]
            
            for descriptions_path in descriptions_paths:
                if path.exists(descriptions_path):
                    # Read and parse the JSON file
                    with open(descriptions_path, 'r') as f:
                        tools = json.load(f)
                        
                        # Format the tools into a readable string
                        result = f'Available tools in GitLab {subdirectory}:\n'
                        for tool_name, description in tools.items():
                            result += f'- {tool_name}: {description}\n'
                        return result.strip()
            
            # If no tool_description.json found, list Python files in the subdirectory
            tools_dirs = [
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/api', site, 'tools', subdirectory),
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/workspace/api', site, 'tools', subdirectory),
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api', site, 'tools', subdirectory)
            ]
            
            for tools_dir in tools_dirs:
                if path.exists(tools_dir):
                    try:
                        tool_files = [
                            f for f in os.listdir(tools_dir)
                            if f.endswith('.py') and not f.startswith('__')
                        ]
                        tool_names = [f[:-3] for f in tool_files]  # Remove .py extension
                        return f'Available tools in GitLab {subdirectory}:\n' + '\n'.join(
                            f'- {name}' for name in tool_names
                        )
                    except Exception:
                        continue
            
            return f"No tools found in GitLab subdirectory '{subdirectory}'"
        
        # If GitLab but no subdirectory specified, list available subdirectories
        elif site == 'gitlab' and not subdirectory:
            tools_dirs = [
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/api', site, 'tools'),
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/workspace/api', site, 'tools'),
                path.join('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api', site, 'tools')
            ]
            
            for tools_dir in tools_dirs:
                if path.exists(tools_dir):
                    try:
                        subdirs = [
                            d for d in os.listdir(tools_dir)
                            if path.isdir(path.join(tools_dir, d)) and not d.startswith('__')
                        ]
                        return 'Available GitLab tool categories:\n' + '\n'.join(
                            f'- {subdir}' for subdir in sorted(subdirs)
                        )
                    except Exception:
                        continue
            
            return "No GitLab tool categories found"
        
        # Standard handling for other sites
        # Look for the tool_descriptions.json file in both potential locations
        descriptions_paths = [
            path.join('/Users/jianhaonan/Desktop/API-Based-Agent/api', site, 'tool_descriptions.json'),
            path.join('/Users/jianhaonan/Desktop/API-Based-Agent/workspace/api', site, 'tool_descriptions.json'),
            path.join('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api', site, 'tool_descriptions.json')
        ]
        
        for descriptions_path in descriptions_paths:
            if path.exists(descriptions_path):
                # Read and parse the JSON file
                with open(descriptions_path, 'r') as f:
                    tools = json.load(f)
                    
                    # Format the tools into a readable string
                    result = 'Available tools:\n'
                    for tool_name, description in tools.items():
                        result += f'- {tool_name}: {description}\n'
                    return result.strip()
        
        # If we get here, try both potential tool directories
        tools_dirs = [
            path.join('/Users/jianhaonan/Desktop/API-Based-Agent/api', site, 'tools'),
            path.join('/Users/jianhaonan/Desktop/API-Based-Agent/workspace/api', site, 'tools'),
            path.join('/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/api', site, 'tools')
        ]
        
        for tools_dir in tools_dirs:
            if path.exists(tools_dir):
                try:
                    tool_files = [
                        f for f in os.listdir(tools_dir)
                        if f.endswith('.py') and not f.startswith('__')
                    ]
                    tool_names = [f[:-3] for f in tool_files]  # Remove .py extension
                    return 'Available tools:\n' + '\n'.join(
                        f'- {name}' for name in tool_names
                    )
                except Exception:
                    continue
        
        return f"No tools directory or descriptions file found for site '{site}'"
    except Exception as e:
        return f'Error getting tools list: {str(e)}'


def get_extra_user_info(site=''):
    output = ''
    if site == '':
        return ''
    if 'gitlab' in site:
        output += 'On gitlab, my *name* is Byte Blaze; My *username* on gitlab is byteblaze; and my *user id* is 2330.'
    if 'shopping' in site and 'shopping_admin' not in site:
        output += 'On the shopping website, my name is Emma Lopez, and my email is emma.lopez@gmail.com. You should use these information if the task asks about *me*, and you should filter out information about me if the task asks about anything related to me.\n'
    if 'shopping_admin' in site:
        output += 'For shopping_admin, your API calling endpoint is `http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default`; '
        return output
    if 'map' in site:
        output += 'For the map website, you will be provided with three sets of APIs, each providing different functionalities; '
        return output
    if 'reddit' in site:
        output += 'On reddit, my username is MarvelsGrantMan136. '
    return output


def extract_sku_from_shopping_html(url):
    html_response = requests.get(url)
    html_content = html_response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    form_tag = soup.find('form', {'id': 'product_addtocart_form'})
    if form_tag:
        data_product_sku = form_tag.get('data-product-sku')
        return data_product_sku
    return ''


def extract_shopping_admin_product(url):
    return url.split('/')[-2]


def get_task_start_url_prompt(task_start_url, site_name, site_base):
    if 'gitlab' in site_name.lower():
        if task_start_url == site_base:
            return ''
        new_url = task_start_url.split(site_base)[1][1:]
        return f'\nThis task is related to the project: `{new_url}`.'
    if 'shopping' == site_name.lower():
        with open(
            '/API-Based-Agent/evaluation/webarena/workspace_utils.py',
            'r',
        ) as f:
            utils_py = f.read()
        task_start_urls = [
            task_start_url.strip() for task_start_url in task_start_url.split('|AND|')
        ]
        if task_start_url == site_base:
            task_start_urls = []
        utils_py = utils_py.replace(
            "'html_page_shopping_abcdefg'", f'{task_start_urls}'
        )
        with open(
            '/API-Based-Agent/workspace/utils.py', 'w'
        ) as f:
            f.write(utils_py)
        if task_start_url == site_base:
            return ''
        if ' |AND| ' in task_start_url:
            prompt = 'This task is related to the following products: '
            skus = {
                task_start_url: extract_sku_from_shopping_html(task_start_url)
                for task_start_url in task_start_urls
            }
            prompt += '; '.join(
                [
                    f'product with sku {skus[task_start_url]} (url: {task_start_url})'
                    for task_start_url in task_start_urls
                ]
            )
            return '\n' + prompt
        else:
            return f'\nThis task is related to the product with sku {extract_sku_from_shopping_html(task_start_url)}; the url of this product is {task_start_url}'
    if 'shopping_admin' in site_name.lower():
        if task_start_url == site_base:
            return ''
        return f'\nThis task is related to the product with product id `{extract_shopping_admin_product(task_start_url)}`.'
    if 'map' in site_name.lower():
        return ''
    if 'reddit' in site_name.lower():
        if task_start_url == site_base:
            return ''
        splits = task_start_url.split('/')
        forum = splits[4]
        comment_id = ''
        if len(splits) > 5:
            comment_id = splits[5]
        if comment_id == '':
            return f'\nThis task is related to the forum {forum}. '
        return f'\nThis task is related to the comment with comment id {comment_id} from the forum {forum}. '
    else:
        assert 1 == 2


def get_browsing_prompt(task_start_url):
    if ' |AND| ' in task_start_url:
        task_start_urls = [
            task_start_url.strip() for task_start_url in task_start_url.split('|AND|')
        ]
        return f"\nFor web browsing, You should start from the URLs {' and '.join(task_start_urls)}, and these webpages are already logged in and opened for you."
    else:
        return f'\nFor web browsing, You should start from the URL {task_start_url}, and this webpage is already logged in and opened for you.'


def get_api_prompt(site_name):
    output = ''
    if 'gitlab' in site_name.lower():
        # For GitLab, only show categories and require agents to call list_tools for each category
        categories = ['commits', 'projects', 'groups', 'issues', 'merge_requests', 'users', 
                     'repositories', 'repository_files', 'members', 'milestones', 'notes', 
                     'todos', 'runners', 'snippets', 'epic', 'misc', 'project_templates']
        
        output += (
            '\nFor the gitlab website, use the following tools to interact with the API:'
            "\n\n1. list_tools(site='gitlab', subdirectory='category') - Lists available tools in a specific category"
            "\n2. get_documentation(tool_name, site='gitlab', category) - Shows documentation for a specific tool"
            "\n3. call_function(tool_name, site='gitlab', category, **kwargs) - Calls the tool with keyword arguments"
            "\n4. get_response(response_id) - Retrieves a stored API response"
            '\n\nGitLab tools are organized into categories. Here are the available categories:'
        )
        
        # Only list the category names, not the tools within them
        for category in categories:
            output += f'\n- {category}'
        
        output += (
            '\n\n**IMPORTANT GUIDELINES:**'
            '\n1. NEVER assume or hardcode any parameter values (like project_id). All required parameters can and should be retrieved using the appropriate tools.'
            '\n2. ALWAYS use project tools first to find project IDs before using tools from other categories.'
            '\n3. You can list tools in multiple categories at once using list_tools(site="gitlab", subdirectory=["commits", "projects"])'
            '\n4. All values needed for API calls can be obtained through API tools - do not ask users to provide IDs or other parameters.'
            '\n5. You MUST use <execute_ipython> tags to run Python code, NOT regular code blocks with triple backticks (```). Code blocks with triple backticks will be treated as text messages and will not execute.'
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import list_tools, get_documentation, call_function, get_response"
            "\n# First, list tools in the projects category to find project ID tools"
            "\nlist_tools(site='gitlab', subdirectory='projects')"
            "\n# Get documentation for a tool to find project ID"
            "\nget_documentation('list_projects', site='gitlab', category='projects')"
            "\n# Call the function to find the project ID"
            "\nprojects = call_function('list_projects', site='gitlab', category='projects')"
            "\n# Extract the project ID for the repository we need"
            "\nproject_id = None"
            "\nfor project in projects['content']:"
            "\n    if 'repository_name' in project and project['repository_name'] == 'target_repo':"
            "\n        project_id = project['id']"
            "\n        break"
            "\n# Now use the project ID with tools from another category"
            "\nlist_tools(site='gitlab', subdirectory='commits')"
            "\nget_documentation('get_commit', site='gitlab', category='commits')"
            "\ncommit_info = call_function('get_commit', site='gitlab', category='commits', project_id=project_id, commit_sha='main')"
            "\n</execute_ipython>"
        )
    
    if 'shopping' in site_name.lower() and 'admin' not in site_name.lower():
        # Get shopping tools
        tools_list = get_tools_list_for_prompt('shopping')
        
        output += (
            '\nFor the shopping website, use the following tools to interact with the API:'
            "\n\n1. get_documentation(tool_name, site='shopping') - Shows documentation for a specific tool"
            "\n2. call_function(tool_name, site='shopping', **kwargs) - Calls the tool with keyword arguments"
            "\n3. get_response(response_id) - Retrieves a stored API response"
            f'\n\n**AVAILABLE TOOLS:**\n{tools_list}'
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import get_documentation, call_function, get_response"
            "\n# Get documentation for a specific tool"
            "\nget_documentation('search_products', site='shopping')"
            "\n# Call the function with appropriate parameters"
            "\nresults = call_function('search_products', site='shopping', search_field='name', search_value='laptop')"
            "\n</execute_ipython>"
            "\n\n*Note that I am Emma Lopez, and my email is emma.lopez@gmail.com.* If the search tool has the suffix 'admin', it returns information about all users. You should find only the information relevant to me if the task asks about anything related to me."
            "\n\nFor tasks involving shopping carts, you must first create a shopping cart using the appropriate cart creation tool before checking carts or adding products. Always use the tools for cart operations instead of direct URL manipulation."
            "\n\n**IMPORTANT:** Do NOT attempt to browse the web directly for shopping operations. Instead, ALWAYS use the API tools provided through the `get_documentation` and `call_function` utilities. Web browsing will not work for these tasks."
        )
    
    if 'shopping_admin' in site_name.lower():
        # Get shopping admin tools
        tools_list = get_tools_list_for_prompt('shopping_admin')
        
        output += (
            '\nFor the shopping admin website, use the following tools to interact with the API:'
            "\n\n1. get_documentation(tool_name, site='shopping_admin') - Shows documentation for a specific tool"
            "\n2. call_function(tool_name, site='shopping_admin', **kwargs) - Calls the tool with keyword arguments"
            "\n3. get_response(response_id) - Retrieves a stored API response"
            "\n4. Note that you should respond with the product name instead of the product id if it's not specified in the task; for customer information, you should respond with the customer name instead of the customer id"
            f'\n\n**AVAILABLE TOOLS:**\n{tools_list}'
            '\n\nExample workflow:' 
            'Make sure you use <execute_ipython> to run the code.'
            "\n<execute_ipython>\nfrom utils import get_documentation, call_function, get_response"
            "\n# Get documentation for a specific tool"
            "\nget_documentation('search_orders', site='shopping_admin')"
            "\n# Call the function with appropriate parameters"
            "\norders = call_function('search_orders', site='shopping_admin', status='pending')"
            "\n</execute_ipython>"
        )
    
    if 'wikipedia' in site_name.lower():
        # Get wikipedia tools
        tools_list = get_tools_list_for_prompt('wikipedia')
        
        output += (
            '\nFor the wikipedia website, use the following tools to interact with the API:'
            "\n\n1. get_documentation(tool_name, site='wikipedia') - Shows documentation for a specific tool"
            "\n2. call_function(tool_name, site='wikipedia', **kwargs) - Calls the tool with keyword arguments"
            "\n3. call_direct(method, url, headers, body, site='wikipedia') - For custom API calls"
            f'\n\n**AVAILABLE TOOLS:**\n{tools_list}'
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import get_documentation, call_function"
            "\n# Get documentation for a specific tool"
            "\nget_documentation('search_library', site='wikipedia')"
            "\n# Call the function with search parameters"
            "\nresults = call_function('search_library', site='wikipedia', pattern='artificial intelligence')"
            "\n</execute_ipython>"
        )
    
    if 'map' in site_name.lower():
        # Get map tools
        tools_list = get_tools_list_for_prompt('map')
        
        output += (
            '\nFor the map website, use the following tools to interact with the API:'
            "\n\n1. get_documentation(tool_name, site='map') - Shows documentation for a specific tool"
            "\n2. call_function(tool_name, site='map', **kwargs) - Calls the tool with keyword arguments"
            "\n3. call_direct(method, url, headers, body, site='map') - For custom API calls"
            f'\n\n**AVAILABLE TOOLS:**\n{tools_list}'
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import get_documentation, call_function"
            "\n# Get documentation for a specific tool"
            "\nget_documentation('search_GET', site='map')"
            "\n# Call the function with search parameters"
            "\nresults = call_function('search_GET', site='map', q='restaurants', format='json')"
            "\n</execute_ipython>"
        )
    
    return output


def get_initial_prompt(
    site_name, site_base, task, api_info, api_token='', extra_user_info=''
):
    # obtain the intent
    intent = task['intent']
    task_start_url = task['start_url']
    intent = f'Think step by step to perform the following task related to {site_name}. Answer the question: ***{intent}***'
    
    
    # Add the API prompt
    intent += get_api_prompt(site_name)
    
    # Add explicit instruction to use API instead of browsing for all sites
    intent += "\n\n**IMPORTANT:** You should use the API tools provided rather than attempting to browse the web directly. Direct web browsing will not work properly for these tasks."
    
    return intent


# print(get_initial_prompt('shopping_admin', 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/admin', {'intent': 'intent-example', 'start_url': "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/admin/catalog/product/edit/id/1481/"}, 'api_info-example', '', 'extra-user-info'))


def get_initial_prompt_multi(sites, task):
    # obtain the intent
    intent = task['intent']
    task_start_url = task['start_url']

    # Check if we're actually dealing with a single site despite using the multi-site function
    if len(sites.keys()) == 1:
        site_name = list(sites.keys())[0]
        return get_initial_prompt(
            site_name,
            sites[site_name]['site_base'],
            task,
            sites[site_name]['api_info'],
            sites[site_name]['api_token'],
            sites[site_name]['extra_user_info'],
        )

    # Continue with original multi-site logic for 2+ sites
    intent = f"Think step by step to perform the following task related to {' and '.join(sites.keys())}. Answer the question: ***{intent}***"
    for site_name in sites.keys():
        intent += f'\nThe site URL for {site_name} is {sites[site_name]["site_base"]}, use this instead of the normal {site_name} URL. '
    for site_name in sites.keys():
        if sites[site_name]['site_base'] in task_start_url:
            intent += get_task_start_url_prompt(
                task_start_url, site_name, sites[site_name]['site_base']
            )
    for site_name in sites.keys():
        if sites[site_name]['api_token'] != '':
            intent += f"\nFor API calling on {site_name}, use this access token: {sites[site_name]['api_token']}"
    for site_name in sites.keys():
        intent += (
            '\n' + sites[site_name]['extra_user_info'] + get_extra_user_info(site_name)
        )
    for site_name in sites.keys():
        # Add the API prompt for each site (this now includes the tools directly)
        intent += get_api_prompt(site_name)
    return intent


sites = {
    'shopping': {
        'site_base': 'shopping_site_base',
        'api_info': 'shopping_api_info',
        'api_token': 'shopping_api_token',
        'extra_user_info': 'shopping_extra_user_info',
    },
    'reddit': {
        'site_base': 'reddit_site_base',
        'api_info': 'reddit_api_info',
        'api_token': 'reddit_api_token',
        'extra_user_info': 'reddit_extra_user_info',
    },
}
# Remove the print that's causing confusion during execution
# print(get_initial_prompt_multi(sites, {'intent': 'intent-example', 'start_url': "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/admin/catalog/product/edit/id/1481/"}))
