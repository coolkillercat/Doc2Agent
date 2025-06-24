import requests
import json
from urllib.parse import urlencode

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of products matching the specified search criteria along with their detailed attributes, media, pricing information, and search metadata.
    """
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
    return "Bearer " + response.json()

def search_products_with_and_conditions(and_conditions: list, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for products using multiple filter conditions with logical AND between conditions.
    
    Args:
        and_conditions: List of dictionaries, each containing 'field', 'value', and optionally 'condition_type'
        page_size: Maximum number of items to return
        current_page: Page number to return
        sort_by: Field to sort results by
        sort_direction: Sort direction ('ASC' or 'DESC')
        return_fields: List of fields to include in the response
        
    Returns:
        Returns a list of products that match all specified search conditions, including product details, attributes, and search metadata."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    
    # Building search criteria parameters
    params = {}
    
    # Add filter groups (AND conditions)
    for i, condition in enumerate(and_conditions):
        params[f'searchCriteria[filter_groups][{i}][filters][0][field]'] = condition['field']
        params[f'searchCriteria[filter_groups][{i}][filters][0][value]'] = condition['value']
        if 'condition_type' in condition:
            params[f'searchCriteria[filter_groups][{i}][filters][0][condition_type]'] = condition['condition_type']
    
    # Add sort order if specified
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add pagination if specified
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add fields to return if specified
    if return_fields:
        params['fields'] = f"items[{','.join(return_fields)}]"
    
    # Headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }
    
    # Make the request
    url = f"{BASE_URL}/rest/default/V1/products?{urlencode(params)}"
    response = requests.get(url, headers=headers)
    
    return response

if __name__ == '__main__':
    # Example usage - search for products with price between 40 and 50
    r = search_products_with_and_conditions([
        {'field': 'price', 'value': '40', 'condition_type': 'gteq'},
        {'field': 'price', 'value': '50', 'condition_type': 'lteq'}
    ], page_size=10, sort_by='name', sort_direction='ASC')
    
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