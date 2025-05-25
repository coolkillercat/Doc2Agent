import requests
from bs4 import BeautifulSoup


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
            '/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena/workspace_utils.py',
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
            '/Users/jianhaonan/Desktop/API-Based-Agent/workspace/utils.py', 'w'
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
        output += (
            '\nNote: Before actually using a Gitlab API call, *you should call the `get_api_documentation_gitlab` function in the `utils` module to get detailed API documentation of the API.* '
            'For example, if you want to use the API GET /api/v4/projects/{id}/repository/commits, you should first do: '
            "\n<execute_ipython>\nfrom utils import get_api_documentation_gitlab\nget_api_documentation_gitlab('GET /api/v4/projects/{id}/repository/commits')\n</execute_ipython>"
            '\nThis will provide you with detailed descriptions of the input parameters and example output jsons.'
        )
    if 'shopping' in site_name.lower() and 'admin' not in site_name.lower():
        output += (
            '\nFor the shopping website, use the following tools to interact with the API:'
            "\n\n1. list_tools(site='shopping') - Lists all available API tools"
            "\n2. get_documentation(tool_name, site='shopping') - Shows documentation for a specific tool"
            "\n3. call_function(tool_name, site='shopping', **kwargs) - Calls the tool with keyword arguments"
            "\n4. call_direct(method, url, headers, body, site='shopping') - For PUT/DELETE operations"
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import list_tools, get_documentation, call_function\nlist_tools(site='shopping')\n</execute_ipython>"
        )
    if 'shopping_admin' in site_name.lower():
        output += (
            '\nFor the shopping admin website, use the following tools to interact with the API:'
            "\n\n1. list_tools(site='shopping_admin') - Lists all available API tools"
            "\n2. get_documentation(tool_name, site='shopping_admin') - Shows documentation for a specific tool"
            "\n3. call_function(tool_name, site='shopping_admin', **kwargs) - Calls the tool with keyword arguments"
            "\n4. call_direct(method, url, headers, body, site='shopping_admin') - For PUT/DELETE operations"
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import list_tools, get_documentation, call_function\nlist_tools(site='shopping_admin')\n</execute_ipython>"
        )
    if 'wikipedia' in site_name.lower():
        output += (
            '\nFor the wikipedia website, use the following tools to interact with the API:'
            "\n\n1. list_tools(site='wikipedia') - Lists all available API tools"
            "\n2. get_documentation(tool_name, site='wikipedia') - Shows documentation for a specific tool"
            "\n3. call_function(tool_name, site='wikipedia', **kwargs) - Calls the tool with keyword arguments"
            "\n4. call_direct(method, url, headers, body, site='wikipedia') - For custom API calls"
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import list_tools, get_documentation, call_function\nlist_tools(site='wikipedia')\n</execute_ipython>"
        )
    if 'map' in site_name.lower():
        output += (
            '\nFor the map website, use the following tools to interact with the API:'
            "\n\n1. list_tools(site='map') - Lists all available API tools"
            "\n2. get_documentation(tool_name, site='map') - Shows documentation for a specific tool"
            "\n3. call_function(tool_name, site='map', **kwargs) - Calls the tool with keyword arguments"
            "\n4. call_direct(method, url, headers, body, site='map') - For custom API calls"
            '\n\nExample workflow:'
            "\n<execute_ipython>\nfrom utils import list_tools, get_documentation, call_function\nlist_tools(site='map')\n</execute_ipython>"
        )
    return output


def get_initial_prompt(
    site_name, site_base, task, api_info, api_token='', extra_user_info=''
):
    # obtain the intent
    intent = task['intent']
    task_start_url = task['start_url']
    intent = f'Think step by step to perform the following task related to {site_name}. Answer the question: ***{intent}***'
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
        intent += (
            f"\n\nBelow is the list of all APIs you can use for {site_name} and their descriptions:"
            f"\n{sites[site_name]['api_info']}"
        )
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
