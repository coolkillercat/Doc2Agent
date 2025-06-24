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


def search_products_with_multiple_filters(filters: list[tuple], logical_operator: str = 'AND', page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC') -> dict:
    """
    Search for products using multiple filter criteria with specified logical relationships (AND/OR).
    
    Args:
        filters: List of tuples, each containing (field, value, condition_type)
        logical_operator: 'AND' or 'OR' to specify how filters should be combined
        page_size: Number of items per page
        current_page: Current page number
        sort_by: Field to sort results by
        sort_direction: 'ASC' or 'DESC' for sort order
    
    Returns:
        API response as dictionary
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    params = {}
    
    if logical_operator == 'OR':
        # All filters in single filter group for OR
        for i, (field, value, condition_type) in enumerate(filters):
            params[f'searchCriteria[filter_groups][0][filters][{i}][field]'] = field
            params[f'searchCriteria[filter_groups][0][filters][{i}][value]'] = value
            params[f'searchCriteria[filter_groups][0][filters][{i}][condition_type]'] = condition_type
    else:
        # Each filter in separate filter group for AND
        for i, (field, value, condition_type) in enumerate(filters):
            params[f'searchCriteria[filter_groups][{i}][filters][0][field]'] = field
            params[f'searchCriteria[filter_groups][{i}][filters][0][value]'] = value
            params[f'searchCriteria[filter_groups][{i}][filters][0][condition_type]'] = condition_type
    
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
        
    response = requests.get(
        f'{ENDPOINT}/rest/default/V1/products',
        headers=headers,
        params=params
    )
    
    return response

if __name__ == '__main__':
    # Example usage: search for products with price between 40 and 49.99
    filters = [
        ('price', '40', 'gteq'),
        ('price', '49.99', 'lteq')
    ]
    r = search_products_with_multiple_filters(
        filters=filters,
        logical_operator='AND',
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
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))