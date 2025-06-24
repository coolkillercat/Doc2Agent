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


def get_product_link_type_attributes(type):
    """
    Retrieve a list of product link type attributes.
    
    Args:
        type (str): The product link type (e.g., 'related', 'upsell', 'crosssell')
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> response = get_product_link_type_attributes(type='related')
        >>> print(response.status_code)
        200
        >>> print(response.json())
        [{"code":"position","type":"int"}]
    """
    assert type is not None, 'Missing required parameter: type'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/products/links/{quote(type, safe='')}/attributes"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_product_link_type_attributes(type='related')
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