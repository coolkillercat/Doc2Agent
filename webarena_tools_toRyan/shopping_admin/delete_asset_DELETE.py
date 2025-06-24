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

def delete_asset(id):
    """
    Delete an Adobe Stock asset by ID.
    
    Args:
        id (int): The ID of the asset to delete.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> response = delete_asset(123)
        >>> print(response.status_code)
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/adobestock/asset/{id}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.delete(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = delete_asset(id=123)
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