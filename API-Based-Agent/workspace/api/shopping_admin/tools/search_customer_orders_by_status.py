import requests, json
from urllib.parse import quote

import requests
import json
def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A response object containing order search results. The response includes a status code, text representation, and a JSON object with an "items" array containing the matching orders. Each order in the items array includes details such as order ID, customer information, status, and other order-specific data based on the search criteria provided in the request.
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



def search_customer_orders_by_status(customer_id: int, status: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for a customer's orders with a specific status, useful for customer service and order tracking.
    
    Args:
        customer_id (int): The ID of the customer whose orders to search
        status (str): The order status to filter by (e.g., 'pending', 'processing', 'complete')
        page_size (int, optional): Number of results to return per page
        current_page (int, optional): Page number to return
        sort_by (str, optional): Field to sort results by (e.g., 'created_at')
        sort_direction (str, optional): Sort direction - 'ASC' or 'DESC' (default)
        return_fields (list, optional): List of fields to return in the response
        
    Returns:
        Returns a list of customer orders filtered by their status, including creation date and order identifiers."""
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    endpoint = f'{base_url}/rest/default/V1/orders'
    
    # Build the search criteria for customer_id and status
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'customer_id',
        'searchCriteria[filter_groups][0][filters][0][value]': customer_id,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'eq',
        'searchCriteria[filter_groups][1][filters][0][field]': 'status',
        'searchCriteria[filter_groups][1][filters][0][value]': status,
        'searchCriteria[filter_groups][1][filters][0][condition_type]': 'eq'
    }
    
    # Add pagination if specified
    if page_size:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add sorting if specified
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add specific fields to return if specified
    if return_fields:
        params['fields'] = f"items[{','.join(return_fields)}]"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = search_customer_orders_by_status(
        customer_id=3, 
        status='pending',
        page_size=10,
        sort_by='created_at',
        return_fields=['increment_id', 'entity_id', 'status', 'created_at']
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