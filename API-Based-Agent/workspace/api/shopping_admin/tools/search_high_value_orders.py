import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A response object containing order information that matches the specified value threshold. The response includes a status code, response text, and a JSON object with an "items" array containing matching order details. Each item in the array represents an order with its complete information including customer data, payment details, totals, and line items, allowing developers to identify and process high-value orders.
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

def search_high_value_orders(minimum_amount: float = 100.0, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Identifies orders with a total value above the specified threshold, useful for VIP customer service or fraud detection.
    
    Args:
        minimum_amount (float): Minimum grand total threshold for orders to return (default: 100.0)
        page_size (int, optional): Maximum number of results to return
        current_page (int, optional): Page number to return
        sort_by (str, optional): Field to sort results by (e.g. 'grand_total', 'created_at')
        sort_direction (str, optional): Sort direction - 'ASC' or 'DESC' (default: 'DESC')
        return_fields (list, optional): List of fields to return in the response
        
    Returns:
        Returns a list of orders that exceed a specified minimum value threshold with customer information and order details."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    endpoint = f"{base_url}/rest/default/V1/orders"
    
    # Build the query parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'grand_total',
        'searchCriteria[filter_groups][0][filters][0][value]': minimum_amount,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gteq'
    }
    
    # Add pagination parameters if provided
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add sorting parameters if provided
    if sort_by is not None:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add fields parameter if specified
    if return_fields is not None:
        fields_str = ','.join(return_fields) if isinstance(return_fields, list) else return_fields
        params['fields'] = f'items[{fields_str}]'
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = search_high_value_orders(
        minimum_amount=150.0,
        page_size=10,
        sort_by='grand_total',
        sort_direction='DESC',
        return_fields=['increment_id', 'entity_id', 'customer_email', 'grand_total']
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