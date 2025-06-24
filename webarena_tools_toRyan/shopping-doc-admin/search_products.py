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


def search_products(field: str, value: str, condition_type: str = 'eq', page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC') -> dict:
    """
    Search for products using a single filter criterion. Allows filtering by any product attribute with customizable condition types.
    
    Args:
        field (str): Product attribute to filter by
        value (str): Value to filter for
        condition_type (str, optional): Type of comparison. Defaults to 'eq'
        page_size (int, optional): Number of items per page. Defaults to None
        current_page (int, optional): Page number to return. Defaults to None
        sort_by (str, optional): Field to sort by. Defaults to None
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC'). Defaults to 'DESC'

    Returns:
        requests.Response: API response object
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    endpoint = f'{base_url}/rest/default/V1/products'
    
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': field,
        'searchCriteria[filter_groups][0][filters][0][value]': value,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': condition_type
    }
    
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
        
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = search_products(field='sku', value='B09KBNDTWJ', condition_type='like')
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