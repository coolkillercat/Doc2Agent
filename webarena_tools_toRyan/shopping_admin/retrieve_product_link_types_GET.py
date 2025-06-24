import requests
import json
from urllib.parse import quote

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


def retrieve_product_link_types(base_url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770', timeout=50, verify=False):
    """
    Retrieve information about available product link types.
    
    Args:
        base_url (str): Base URL for the API. Default is 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'.
        timeout (int): Request timeout in seconds. Default is 50.
        verify (bool): Whether to verify SSL certificates. Default is False.
    
    Returns:
        requests.Response: The API response object containing product link types.
        
    Example:
        >>> response = retrieve_product_link_types()
        >>> link_types = response.json()
        >>> print(link_types)
        [{'code': 1, 'name': 'related'}, {'code': 5, 'name': 'crosssell'}, ...]
    """
    api_url = f"{base_url}/rest/default/V1/products/links/types"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=timeout, verify=verify)
    return response

if __name__ == '__main__':
    r = retrieve_product_link_types()
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