import requests
import json
from urllib.parse import urlencode

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of pending orders with comprehensive details including customer information, billing/shipping addresses, payment information, order items, and financial summaries.
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

def search_pending_orders(page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Retrieves all pending orders that require processing, useful for order fulfillment workflows.
    
    Args:
        page_size (int, optional): Maximum number of items to return.
        current_page (int, optional): The current page number.
        sort_by (str, optional): Field to sort results by.
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC'). Defaults to 'DESC'.
        return_fields (list, optional): List of fields to return in the response.
    
    Returns:
        Returns a list of pending orders with detailed information including customer data, financial details, shipping information, and order status."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    # Build the search criteria parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'status',
        'searchCriteria[filter_groups][0][filters][0][value]': 'pending',
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'eq'
    }
    
    # Add optional parameters if provided
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    if sort_by is not None:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    if return_fields is not None:
        fields_str = ','.join(return_fields) if isinstance(return_fields, list) else return_fields
        params['fields'] = fields_str
    
    # Make the API request
    response = requests.get(
        f'{BASE_URL}/rest/default/V1/orders',
        headers=headers,
        params=params
    )
    
    return response

if __name__ == '__main__':
    r = search_pending_orders() # no parameter inputs at current stage, need to be filled later.
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