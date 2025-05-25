import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Authenticate with the provider and get a token.
    
    Returns:
        str: Authentication token for the customer.
    
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def verify_u2f_key(username=None, password=None, publicKeyCredentialJson=None):
    """
    Verify a U2F key for two-factor authentication.
    
    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
        publicKeyCredentialJson (str): JSON string containing the public key credential information.
    
    Returns:
        requests.Response: The response from the API.
    
    Example:
        response = verify_u2f_key(
            username='user@example.com',
            password='password123',
            publicKeyCredentialJson='{"id":"credentialId","rawId":"rawId","response":{"clientDataJSON":"clientData","authenticatorData":"authData","signature":"signature","userHandle":"userHandle"},"type":"public-key"}'
        )
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/tfa/u2f/verify"
    
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    assert publicKeyCredentialJson is not None, 'Missing required parameter: publicKeyCredentialJson'
    
    payload = {
        'username': username, 
        'password': password, 
        'publicKeyCredentialJson': publicKeyCredentialJson
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = verify_u2f_key(username='user@example.com', password='password123', publicKeyCredentialJson='{"id":"credentialId","rawId":"rawId","response":{"clientDataJSON":"clientData","authenticatorData":"authData","signature":"signature","userHandle":"userHandle"},"type":"public-key"}')
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