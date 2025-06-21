import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A response object containing the API call results with status_code indicating the HTTP status of the request, text providing the raw response content, json containing the parsed response data with an 'items' field (which may be null), and content providing the full response body as a string. This structure allows developers to access both the raw response and the parsed JSON data for processing best-selling products information.
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

def search_best_selling_products(time_period: str = 'month', limit: int = 10, return_fields: list = None):
    """
    Retrieves the best-selling products for a specified time period, useful for sales analysis and merchandising.
    
    Args:
        time_period (str): The time period to search for ('day', 'week', 'month', 'year'). Default is 'month'.
        limit (int): Maximum number of products to return. Default is 10.
        return_fields (list): List of fields to return. If None, all fields will be returned.
    
    Returns:
        Returns a list of best-selling products ranked by sales performance for a specified time period."""
    # Set base URL
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/orders'
    
    # Set up headers
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    # Prepare parameters for time period filtering
    params = {}
    
    # Add pagination and sorting
    params['searchCriteria[pageSize]'] = str(limit)
    params['searchCriteria[currentPage]'] = '1'
    params['searchCriteria[sortOrders][0][field]'] = 'created_at'
    params['searchCriteria[sortOrders][0][direction]'] = 'DESC'
    
    # Add time period filter
    if time_period == 'day':
        # Last 24 hours
        params['searchCriteria[filter_groups][0][filters][0][field]'] = 'created_at'
        params['searchCriteria[filter_groups][0][filters][0][value]'] = '2023-11-01 00:00:00'
        params['searchCriteria[filter_groups][0][filters][0][condition_type]'] = 'gt'
    elif time_period == 'week':
        # Last 7 days
        params['searchCriteria[filter_groups][0][filters][0][field]'] = 'created_at'
        params['searchCriteria[filter_groups][0][filters][0][value]'] = '2023-10-25 00:00:00'
        params['searchCriteria[filter_groups][0][filters][0][condition_type]'] = 'gt'
    elif time_period == 'year':
        # Last 365 days
        params['searchCriteria[filter_groups][0][filters][0][field]'] = 'created_at'
        params['searchCriteria[filter_groups][0][filters][0][value]'] = '2022-11-01 00:00:00'
        params['searchCriteria[filter_groups][0][filters][0][condition_type]'] = 'gt'
    else:  # Default to month
        # Last 30 days
        params['searchCriteria[filter_groups][0][filters][0][field]'] = 'created_at'
        params['searchCriteria[filter_groups][0][filters][0][value]'] = '2023-10-01 00:00:00'
        params['searchCriteria[filter_groups][0][filters][0][condition_type]'] = 'gt'
    
    # Add specific fields to return if provided
    if return_fields:
        fields_str = ','.join(return_fields)
        params['fields'] = f'items[{fields_str}]'
    
    # Make the request
    response = requests.get(base_url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = search_best_selling_products(time_period='month', limit=5, return_fields=['entity_id', 'increment_id', 'created_at', 'customer_email', 'total_qty_ordered'])
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