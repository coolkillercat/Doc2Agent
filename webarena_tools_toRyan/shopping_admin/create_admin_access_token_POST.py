import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    Get the admin authentication token from the shopping API.
    
    Returns:
        str: Bearer token for authentication
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers = {
            'Content-Type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return "Bearer " + response.json()

def create_admin_access_token(username, password):
    """
    Create an access token for admin given the admin credentials.
    
    Args:
        username (str): Admin username
        password (str): Admin password
    
    Returns:
        requests.Response: Response object from the API
    
    Examples:
        >>> create_admin_access_token('admin', 'admin1234')
        >>> create_admin_access_token('user@example.com', 'secure_password')
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/integration/admin/token"
    
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    
    payload = {
        'username': username,
        'password': password
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(
        url=api_url, 
        data=json.dumps(payload), 
        headers=headers, 
        timeout=50, 
        verify=False
    )
    
    return response

if __name__ == '__main__':
    r = create_admin_access_token(username='admin', password='admin1234')
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