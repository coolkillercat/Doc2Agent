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


def search_with_complex_filters(filter_groups: list[list[tuple]], page_size: int = None, current_page: int = None, sort_by: list[str] = None, sort_directions: list[str] = None, endpoint: str = None, return_fields: list[str] = None) -> dict:
    """
    Perform complex searches with multiple filter groups (AND) containing multiple filters (OR). Supports advanced logical combinations across any API endpoint.
    
    Args:
        filter_groups (list[list[tuple]]): List of filter groups, each containing list of (field, value, condition_type) tuples
        page_size (int, optional): Number of items per page
        current_page (int, optional): Current page number
        sort_by (list[str], optional): Fields to sort by
        sort_directions (list[str], optional): Sort directions ('ASC' or 'DESC') corresponding to sort_by fields
        endpoint (str, optional): API endpoint to query
        return_fields (list[str], optional): Specific fields to return in response
        
    Returns:
        dict: API response
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    endpoint = endpoint or '/rest/default/V1/products'
    url = f"{base_url}{endpoint}"
    
    params = {}
    
    # Build filter groups
    for group_idx, filter_group in enumerate(filter_groups):
        for filter_idx, (field, value, condition_type) in enumerate(filter_group):
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][field]'] = field
            params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][value]'] = value
            if condition_type and condition_type != 'eq':
                params[f'searchCriteria[filter_groups][{group_idx}][filters][{filter_idx}][condition_type]'] = condition_type

    # Add pagination
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    if current_page:
        params['searchCriteria[currentPage]'] = current_page

    # Add sorting
    if sort_by:
        for idx, field in enumerate(sort_by):
            params[f'searchCriteria[sortOrders][{idx}][field]'] = field
            if sort_directions and len(sort_directions) > idx:
                params[f'searchCriteria[sortOrders][{idx}][direction]'] = sort_directions[idx]

    # Add fields to return
    if return_fields:
        params['fields'] = ','.join(return_fields)

    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    return requests.get(url, params=params, headers=headers)

if __name__ == '__main__':
    # Example search for products with price between 40 and 49.99 and SKU like WSH%29% or WP%29%
    filter_groups = [
        [
            ('sku', 'WSH%29%', 'like'),
            ('sku', 'WP%29%', 'like')
        ],
        [
            ('price', '40', 'from')
        ],
        [
            ('price', '49.99', 'to')
        ]
    ]
    
    r = search_with_complex_filters(
        filter_groups=filter_groups,
        page_size=20,
        current_page=1,
        sort_by=['name'],
        sort_directions=['ASC'],
        return_fields=['items[name,sku,price]']
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