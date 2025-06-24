import requests
import json
from datetime import datetime, timedelta

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of orders matching the specified search criteria along with the total count of matching records.
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


def search_recent_orders(hours: int = 24, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Retrieves orders placed within the specified number of hours, useful for monitoring recent sales activity.
    
    Args:
        hours (int): Number of hours to look back for orders. Default is 24.
        page_size (int, optional): Maximum number of items to return per page.
        current_page (int, optional): Page number to return.
        sort_by (str, optional): Field to sort results by (e.g., 'created_at').
        sort_direction (str, optional): Sort direction, either 'ASC' or 'DESC'. Default is 'DESC'.
        return_fields (list, optional): List of fields to return in the response.
    
    Returns:
        Returns a list of orders placed within a specified timeframe along with the total count of matching records."""
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    
    # Calculate the timestamp for the specified hours ago
    time_from = (datetime.now() - timedelta(hours=hours)).strftime('%Y-%m-%d %H:%M:%S')
    
    # Build the query parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'created_at',
        'searchCriteria[filter_groups][0][filters][0][value]': time_from,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gt'
    }
    
    # Add optional parameters
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    if return_fields:
        params['fields'] = ','.join(return_fields)
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(
        url=f'{BASE_URL}/rest/default/V1/orders',
        headers=headers,
        params=params
    )
    
    return response

if __name__ == '__main__':
    r = search_recent_orders() # no parameter inputs at current stage, need to be filled later.
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