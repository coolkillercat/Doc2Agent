import requests, json
from urllib.parse import quote

import requests
import json
def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a collection of orders with comprehensive details including customer information, financial data, shipping details, line items, and status information within the specified date range.
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



def search_orders_by_date_range(start_date: str, end_date: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for orders created within a specific date range, useful for periodic reporting or synchronization.
    
    Args:
        start_date (str): The start date in format 'YYYY-MM-DD HH:MM:SS'
        end_date (str): The end date in format 'YYYY-MM-DD HH:MM:SS'
        page_size (int, optional): Maximum number of items to return
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort by (e.g., 'created_at')
        sort_direction (str, optional): Sort direction, 'ASC' or 'DESC'
        return_fields (list, optional): List of fields to return in the response
        
    Returns:
        Returns a list of orders within a specified date range with comprehensive order details including customer information, financial data, shipping details, and order status."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/orders"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token(),
    }
    
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'created_at',
        'searchCriteria[filter_groups][0][filters][0][value]': start_date,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gteq',
        'searchCriteria[filter_groups][1][filters][0][field]': 'created_at',
        'searchCriteria[filter_groups][1][filters][0][value]': end_date,
        'searchCriteria[filter_groups][1][filters][0][condition_type]': 'lteq'
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
    
    # Add fields filter if specified
    if return_fields is not None:
        fields_str = "items[" + ",".join(return_fields) + "]"
        params['fields'] = fields_str
    
    response = requests.get(base_url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = search_orders_by_date_range("2023-01-01 00:00:00", "2023-12-31 23:59:59", page_size=10, sort_by="created_at")
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