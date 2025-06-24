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


def search_products_by_attributes(attributes: dict, match_all: bool = True, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC') -> dict:
    """
    Search for products matching specific attribute values.
    
    Args:
        attributes (dict): Dictionary of attribute name-value pairs to search for
        match_all (bool): If True, all attributes must match (AND). If False, any attribute can match (OR)
        page_size (int): Number of items per page
        current_page (int): Page number to return
        sort_by (str): Field name to sort results by
        sort_direction (str): Sort direction ('ASC' or 'DESC')
        
    Returns:
        dict: API response containing matching products
    """
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    # Build search criteria
    params = {}
    
    # Add filters
    if match_all:
        # Each attribute gets its own filter group for AND
        for i, (field, value) in enumerate(attributes.items()):
            params[f'searchCriteria[filter_groups][{i}][filters][0][field]'] = field
            params[f'searchCriteria[filter_groups][{i}][filters][0][value]'] = value
            params[f'searchCriteria[filter_groups][{i}][filters][0][condition_type]'] = 'eq'
    else:
        # All attributes in same filter group for OR
        for i, (field, value) in enumerate(attributes.items()):
            params[f'searchCriteria[filter_groups][0][filters][{i}][field]'] = field
            params[f'searchCriteria[filter_groups][0][filters][{i}][value]'] = value
            params[f'searchCriteria[filter_groups][0][filters][{i}][condition_type]'] = 'eq'
    
    # Add pagination
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
        
    # Add sorting
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction

    response = requests.get(
        f'{BASE_URL}/rest/default/V1/products',
        headers=headers,
        params=params
    )
    
    return response

if __name__ == '__main__':
    test_attributes = {
        'name': 'Test Product',
        'price': '99.99'
    }
    r = search_products_by_attributes(
        attributes=test_attributes,
        match_all=True,
        page_size=20,
        current_page=1,
        sort_by='name',
        sort_direction='ASC'
    )
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))