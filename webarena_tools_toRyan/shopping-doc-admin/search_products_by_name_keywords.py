import requests, json
from urllib.parse import quote

import requests
import json
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
    return "Bearer " + response.json()


def search_products_by_name_keywords(keywords: list[str], match_all: bool = False, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC') -> dict:
    """
    Search for products containing specific keywords in their names. Can require all keywords (AND) or any keyword (OR) to match.

    Args:
        keywords (list[str]): List of keywords to search for in product names
        match_all (bool): If True, all keywords must match (AND). If False, any keyword can match (OR)
        page_size (int): Number of items per page
        current_page (int): Page number to return
        sort_by (str): Field to sort results by
        sort_direction (str): Sort direction ('ASC' or 'DESC')

    Returns:
        dict: API response containing matched products
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/products'
    params = []

    if match_all:
        # AND logic - each keyword in separate filter group
        for i, keyword in enumerate(keywords):
            params.append(f"searchCriteria[filter_groups][{i}][filters][0][field]=name")
            params.append(f"searchCriteria[filter_groups][{i}][filters][0][value]=%25{keyword}%25")
            params.append(f"searchCriteria[filter_groups][{i}][filters][0][condition_type]=like")
    else:
        # OR logic - all keywords in same filter group
        for i, keyword in enumerate(keywords):
            params.append(f"searchCriteria[filter_groups][0][filters][{i}][field]=name")
            params.append(f"searchCriteria[filter_groups][0][filters][{i}][value]=%25{keyword}%25")
            params.append(f"searchCriteria[filter_groups][0][filters][{i}][condition_type]=like")

    if page_size:
        params.append(f"searchCriteria[pageSize]={page_size}")
    if current_page:
        params.append(f"searchCriteria[currentPage]={current_page}")
    if sort_by:
        params.append(f"searchCriteria[sortOrders][0][field]={sort_by}")
        params.append(f"searchCriteria[sortOrders][0][direction]={sort_direction}")

    url = f"{base_url}?{'&'.join(params)}"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }

    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = search_products_by_name_keywords(['Bag', 'Leather'], match_all=True, page_size=10)
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))