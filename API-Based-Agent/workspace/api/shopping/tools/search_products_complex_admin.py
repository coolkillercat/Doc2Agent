import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a collection of items that match the specified search criteria, with support for complex filtering conditions.
    """
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

def search_products_complex(and_or_conditions=None, page_size=None, current_page=None, sort_by=None, sort_direction='DESC', return_fields=None):
    """
    Performs complex product searches with both AND and OR logic, supporting nested conditions for advanced filtering.
    
    Parameters:
    and_or_conditions (list): A list of filter conditions where each condition is a dict or list.
                              Dict represents AND condition group, list represents OR conditions within a group.
                              Format: [{'field': 'name', 'value': 'Test', 'condition_type': 'like'}, 
                                       [{'field': 'price', 'value': '10', 'condition_type': 'gt'},
                                        {'field': 'price', 'value': '20', 'condition_type': 'lt'}]]
    page_size (int): Maximum number of items to return
    current_page (int): Current page number
    sort_by (str): Field to sort results by
    sort_direction (str): Sort direction - 'ASC' or 'DESC'
    return_fields (list): List of fields to return in the response
    
    Returns:
        Returns search results for products based on complex filtering conditions with support for nested AND/OR logic.
    requests.Response: API response object
    """
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    endpoint = f"{BASE_URL}/rest/default/V1/products"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    params = {}
    
    # Process filter conditions
    if and_or_conditions:
        filter_group_idx = 0
        for condition_group in and_or_conditions:
            if isinstance(condition_group, dict):
                # Single condition in AND group
                field = condition_group.get('field')
                value = condition_group.get('value')
                condition_type = condition_group.get('condition_type', 'eq')
                
                params[f'searchCriteria[filter_groups][{filter_group_idx}][filters][0][field]'] = field
                params[f'searchCriteria[filter_groups][{filter_group_idx}][filters][0][value]'] = value
                params[f'searchCriteria[filter_groups][{filter_group_idx}][filters][0][condition_type]'] = condition_type
                
                filter_group_idx += 1
            elif isinstance(condition_group, list):
                # Multiple conditions in OR group
                for filter_idx, condition in enumerate(condition_group):
                    field = condition.get('field')
                    value = condition.get('value')
                    condition_type = condition.get('condition_type', 'eq')
                    
                    params[f'searchCriteria[filter_groups][{filter_group_idx}][filters][{filter_idx}][field]'] = field
                    params[f'searchCriteria[filter_groups][{filter_group_idx}][filters][{filter_idx}][value]'] = value
                    params[f'searchCriteria[filter_groups][{filter_group_idx}][filters][{filter_idx}][condition_type]'] = condition_type
                
                filter_group_idx += 1
    
    # Add pagination
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add sorting
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add fields to return
    if return_fields:
        fields_str = ','.join(return_fields)
        params['fields'] = f'items[{fields_str}]'
    
    # Make the request
    response = requests.get(endpoint, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    # Example search for products with price between 10 and 20 OR name containing "Shirt"
    sample_conditions = [
        [
            {'field': 'name', 'value': '%25Shirt%25', 'condition_type': 'like'},
            {'field': 'name', 'value': '%25Tee%25', 'condition_type': 'like'}
        ],
        {'field': 'price', 'value': '50', 'condition_type': 'lt'}
    ]
    
    r = search_products_complex(
        and_or_conditions=sample_conditions,
        page_size=10,
        current_page=1,
        sort_by='name',
        sort_direction='ASC',
        return_fields=['entity_id', 'name', 'price', 'sku']
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