import requests, json
from urllib.parse import quote

import requests
import json
def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of orders with customer email addresses and order identification information.
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



def search_orders_by_status(status: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for orders with a specific status (e.g., 'pending', 'processing', 'complete'), with support for pagination and sorting.
    
    Args:
        status (str): Order status to filter by (e.g., 'pending', 'processing', 'complete')
        page_size (int, optional): Maximum number of items to return per page
        current_page (int, optional): Current page number for pagination
        sort_by (str, optional): Field to sort results by (e.g., 'created_at', 'increment_id')
        sort_direction (str, optional): Sort direction, either 'ASC' or 'DESC'
        return_fields (list, optional): List of fields to return in the response
        
    Returns:
        Returns a list of orders filtered by status, including customer email and order identification details."""
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    endpoint = f'{base_url}/rest/default/V1/orders'
    
    # Build query parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'status',
        'searchCriteria[filter_groups][0][filters][0][value]': status,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'eq'
    }
    
    # Add pagination if specified
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add sorting if specified
    if sort_by is not None:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add fields to return if specified
    if return_fields is not None:
        fields_str = 'items[' + ','.join(return_fields) + ']'
        params['fields'] = fields_str
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, params=params, headers=headers)
    return response

if __name__ == '__main__':
    r = search_orders_by_status('pending', page_size=10, sort_by='created_at', return_fields=['increment_id', 'entity_id', 'customer_email'])
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