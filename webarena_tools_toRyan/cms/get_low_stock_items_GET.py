import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    Get the admin authentication token for the shopping API.
    
    Returns:
        str: The authentication token with 'Bearer ' prefix.
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


def get_low_stock_items(scopeId, qty, currentPage=1, pageSize=20):
    """
    Retrieves a list of SKU's with low inventory quantity.
    
    Args:
        scopeId (int): The scope ID (required).
        qty (float): The quantity threshold for low stock (required).
        currentPage (int, optional): The current page number. Defaults to 1.
        pageSize (int, optional): The number of items per page. Defaults to 20.
    
    Returns:
        Returns a list of SKUs with inventory quantities below a specified threshold.
    Examples:
        >>> response = get_low_stock_items(scopeId=1, qty=10)
        >>> response = get_low_stock_items(scopeId=1, qty=10, currentPage=2, pageSize=50)
    """
    BASE_URL = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    api_url = f"{BASE_URL}/rest/default/V1/stockItems/lowStock/"
    
    # Validate required parameters
    if scopeId is None:
        raise ValueError('Missing required parameter: scopeId')
    if qty is None:
        raise ValueError('Missing required parameter: qty')
    
    # Build query parameters
    querystring = {
        'scopeId': scopeId,
        'qty': qty
    }
    
    # Add optional parameters if provided
    if currentPage is not None:
        querystring['currentPage'] = currentPage
    if pageSize is not None:
        querystring['pageSize'] = pageSize
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(
        url=api_url,
        params=querystring,
        headers=headers,
        timeout=50,
        verify=False
    )
    
    return response


if __name__ == '__main__':
    r = get_low_stock_items(scopeId=1, qty=10, currentPage=1, pageSize=20)
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))