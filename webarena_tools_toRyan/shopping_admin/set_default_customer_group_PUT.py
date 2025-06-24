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


def set_default_customer_group(id):
    """
    Set system default customer group.
    
    Args:
        id (int): The ID of the customer group to set as default.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        >>> response = set_default_customer_group(id=1)
        >>> print(response.status_code)
        200
        >>> print(response.json())
        1
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/customerGroups/default/{id}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.put(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = set_default_customer_group(id=1)
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