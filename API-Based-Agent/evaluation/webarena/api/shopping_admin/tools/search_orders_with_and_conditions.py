import requests, json
from urllib.parse import quote

import requests
import json
def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of orders matching the specified filter conditions.
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



def search_orders_with_and_conditions(and_conditions: list, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for orders using multiple filter conditions with logical AND between conditions.
    
    Args:
        and_conditions: List of dictionaries with filter conditions. Each dict should have 'field', 'value', and optional 'condition_type'.
        page_size: Maximum number of items to return.
        current_page: Page number to return.
        sort_by: Field to sort by.
        sort_direction: Sort direction ('ASC' or 'DESC').
        return_fields: List of fields to return in the response.
        
    Returns:
        Returns order records that match all specified search conditions."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/orders"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    # Build query parameters
    params = {}
    
    # Add filter conditions (AND logic)
    for i, condition in enumerate(and_conditions):
        field = condition.get('field')
        value = condition.get('value')
        condition_type = condition.get('condition_type', 'eq')  # Default to 'eq' if not provided
        
        params[f'searchCriteria[filter_groups][{i}][filters][0][field]'] = field
        params[f'searchCriteria[filter_groups][{i}][filters][0][value]'] = value
        params[f'searchCriteria[filter_groups][{i}][filters][0][condition_type]'] = condition_type
    
    # Add sorting criteria
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add pagination
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
        
    # Add fields to return
    if return_fields:
        fields_str = ','.join(return_fields)
        params['fields'] = fields_str
    
    # Make the request
    response = requests.get(base_url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    # Example usage with sample conditions
    conditions = [
        {'field': 'status', 'value': 'pending'},
        {'field': 'customer_email', 'value': 'jdoe@example.com'}
    ]
    
    r = search_orders_with_and_conditions(
        and_conditions=conditions,
        page_size=10,
        current_page=1,
        sort_by='created_at',
        sort_direction='DESC',
        return_fields=['items[increment_id,entity_id,status]']
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