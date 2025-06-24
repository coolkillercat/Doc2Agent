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

def search_products_by_sku_pattern(sku_pattern: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC') -> dict:
    """
    Search for products with SKUs matching a specific pattern. Uses the like condition type with % wildcards to find matching products.
    
    Args:
        sku_pattern (str): Pattern to match SKUs against
        page_size (int, optional): Number of items per page
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC')
        
    Returns:
        requests.Response: API response containing matching products
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = f"{base_url}/rest/default/V1/products"
    
    # Build search criteria
    search_params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'sku',
        'searchCriteria[filter_groups][0][filters][0][value]': f'%{sku_pattern}%',
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'like'
    }
    
    # Add optional parameters
    if page_size:
        search_params['searchCriteria[pageSize]'] = page_size
    if current_page:
        search_params['searchCriteria[currentPage]'] = current_page
    if sort_by:
        search_params['searchCriteria[sortOrders][0][field]'] = sort_by
        search_params['searchCriteria[sortOrders][0][direction]'] = sort_direction

    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token(),
    }

    response = requests.get(endpoint, headers=headers, params=search_params)
    return response

if __name__ == '__main__':
    r = search_products_by_sku_pattern("24-MB04", page_size=20, current_page=1, sort_by="name")
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