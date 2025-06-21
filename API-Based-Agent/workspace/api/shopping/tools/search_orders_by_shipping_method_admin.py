import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of orders matching the specified shipping method criteria along with search metadata and total count.
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


def search_orders_by_shipping_method(shipping_method: str, page_size: int = None, current_page: int = None, sort_by: str = None, sort_direction: str = 'DESC', return_fields: list = None):
    """
    Searches for orders with a specific shipping method, useful for fulfillment planning and shipping analysis.
    
    Args:
        shipping_method (str): The shipping method to search for
        page_size (int, optional): Maximum number of items to return
        current_page (int, optional): Current page number
        sort_by (str, optional): Field to sort results by
        sort_direction (str, optional): Sort direction ('ASC' or 'DESC')
        return_fields (list, optional): Specific fields to return in the response
        
    Returns:
        Returns a list of orders filtered by shipping method with search metadata and total count."""
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    endpoint = f"{base_url}/rest/default/V1/orders"
    
    # Build the query parameters
    params = {
        'searchCriteria[filter_groups][0][filters][0][field]': 'shipping_method',
        'searchCriteria[filter_groups][0][filters][0][value]': shipping_method,
        'searchCriteria[filter_groups][0][filters][0][condition_type]': 'eq'
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
    
    # Add fields parameter if specific fields are requested
    if return_fields is not None:
        fields_str = ','.join(return_fields) if isinstance(return_fields, list) else return_fields
        params['fields'] = fields_str
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response


if __name__ == '__main__':
    r = search_orders_by_shipping_method('tablerate_bestway', page_size=10, sort_by='created_at')
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