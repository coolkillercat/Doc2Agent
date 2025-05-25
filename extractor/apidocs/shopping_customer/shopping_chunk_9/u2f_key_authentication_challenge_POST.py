import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    response = requests.post(
        url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def u2f_key_authentication_challenge(username=None, password=None):
    """
    Get the information to initiate a WebAuthn authentication ceremony.
    
    Args:
        username (str): The username for authentication. Required.
        password (str): The password for authentication. Required.
        
    Returns:
        requests.Response: The API response object.
        
    Examples:
        >>> u2f_key_authentication_challenge(username='user@example.com', password='password123')
        >>> u2f_key_authentication_challenge(username='user123', password='securepass')
        >>> u2f_key_authentication_challenge(username='admin', password='adminpass')
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/tfa/webauthn/authentication-challenge"
    payload = {'username': username, 'password': password}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = u2f_key_authentication_challenge(username='user@example.com', password='password123')
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