import requests
import json
from datetime import datetime, timedelta
import urllib.parse

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns: A JSON response containing a list of customers who registered within the specified timeframe in the "items" array. The response includes the search criteria used for filtering in the "search_criteria" object and a "total_count" indicating the number of matching customers found. The status code indicates whether the request was successful, and the full response content is available as both parsed JSON and raw text.
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

def search_new_customers(days: int = 30, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Identifies customers who registered within the specified number of days, useful for welcome campaigns and new customer analysis.
    
    Args:
        days (int): Number of days to look back for new customer registrations. Default is 30.
        page_size (int, optional): Maximum number of items to return.
        current_page (int, optional): Page number to return.
        sort_by (str, optional): Field to sort results by.
        sort_direction (str, optional): Sort order, either 'ASC' or 'DESC'. Default is 'DESC'.
        return_fields (list, optional): List of fields to return in the response.
        
    Returns:
        Returns a list of customers who registered within the specified timeframe along with the total count of matching customers."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    endpoint = f"{base_url}/rest/default/V1/customers/search"
    
    # Calculate the date from days ago
    date_from = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
    
    # Build search criteria parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'created_at',
        'searchCriteria[filter_groups][0][filters][0][value]': date_from,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gt'
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
        fields_str = ','.join(return_fields)
        params['fields'] = f'items[{fields_str}]'
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = search_new_customers()  # no parameter inputs at current stage, need to be filled later.
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