import requests, json
from urllib.parse import quote, urlencode

import requests
import json
def get_shopping_admin_auth_token():
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


def paginated_search(endpoint: str, filters: list[tuple], page_size: int = 20, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list[str] = None) -> list:
    """
    Execute a paginated search across multiple pages, automatically handling pagination to return complete result sets for any endpoint.
    
    Args:
        endpoint (str): API endpoint path
        filters (list[tuple]): List of tuples containing (field, value, condition_type)
        page_size (int): Number of items per page
        sort_by (str): Field to sort results by
        sort_direction (str): Sort direction ('ASC' or 'DESC')
        return_fields (list[str]): List of fields to return in response
        
    Returns:
        requests.Response: API response object
    """
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }

    params = {}
    
    # Add filters
    for i, (field, value, condition_type) in enumerate(filters):
        params[f'searchCriteria[filter_groups][0][filters][{i}][field]'] = field
        params[f'searchCriteria[filter_groups][0][filters][{i}][value]'] = value
        if condition_type:
            params[f'searchCriteria[filter_groups][0][filters][{i}][condition_type]'] = condition_type
            
    # Add pagination
    params['searchCriteria[pageSize]'] = page_size
    params['searchCriteria[currentPage]'] = 1
    
    # Add sorting
    if sort_by:
        params['searchCriteria[sortOrders][0][field]'] = sort_by
        params['searchCriteria[sortOrders][0][direction]'] = sort_direction
        
    # Add fields to return
    if return_fields:
        params['fields'] = f"items[{','.join(return_fields)}]"
        
    url = f"{BASE_URL}{endpoint}"
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    # Example usage
    filters = [
        ('status', 'pending', 'eq'),
        ('created_at', '2023-01-01 00:00:00', 'gt')
    ]
    r = paginated_search(
        endpoint='/rest/default/V1/orders',
        filters=filters,
        page_size=10,
        sort_by='created_at',
        sort_direction='DESC',
        return_fields=['increment_id', 'entity_id']
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