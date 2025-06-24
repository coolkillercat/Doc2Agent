import requests
import json
from datetime import datetime, timedelta

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of products that match the specified search criteria along with the total count of matching items.
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


def search_recently_updated_products(hours: int = 24, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Retrieves products that have been updated within the specified number of hours, useful for monitoring product catalog changes.
    
    Args:
        hours (int): Number of hours to look back for product updates (default: 24)
        page_size (int, optional): Maximum number of items to return per page
        current_page (int, optional): Page number to return
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction, either 'ASC' or 'DESC' (default: 'DESC')
        return_fields (list, optional): List of fields to return in the response
        
    Returns:
        Returns a list of products that have been updated within a specified time period along with the total count of matching items."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    endpoint = f"{base_url}/rest/default/V1/products"
    
    # Calculate the timestamp for 'hours' ago
    timestamp = (datetime.now() - timedelta(hours=hours)).strftime('%Y-%m-%d %H:%M:%S')
    
    # Build the query params
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'updated_at',
        'searchCriteria[filter_groups][0][filters][0][value]': timestamp,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gt'
    }
    
    # Add sorting if specified
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
    
    # Add pagination if specified
    if page_size is not None:
        params['searchCriteria[pageSize]'] = page_size
    
    if current_page is not None:
        params['searchCriteria[currentPage]'] = current_page
    
    # Add fields parameter if specified
    if return_fields:
        fields_str = ','.join(return_fields)
        params['fields'] = fields_str
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, params=params, headers=headers)
    return response


if __name__ == '__main__':
    r = search_recently_updated_products()
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