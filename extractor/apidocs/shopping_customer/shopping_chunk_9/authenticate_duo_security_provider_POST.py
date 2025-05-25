import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get a customer authentication token from the Magento API.
    
    Returns:
        str: Authentication token for the customer
        
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

def authenticate_duo_security_provider(username=None, password=None, signatureResponse=None):
    """
    Authenticate a user with Duo Security provider.
    
    Args:
        username (str): The username for authentication
        password (str): The password for authentication
        signatureResponse (str): The signature response from Duo Security
        
    Returns:
        requests.Response: The response from the authentication request
        
    Example:
        response = authenticate_duo_security_provider(
            username='user@example.com',
            password='password123',
            signatureResponse='sigResponse123'
        )
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/V1/tfa/provider/duo_security/authenticate"
    payload = {'username': username, 'password': password, 'signatureResponse': signatureResponse}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    assert signatureResponse is not None, 'Missing required parameter: signatureResponse'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = authenticate_duo_security_provider(username='user@example.com', password='password123', signatureResponse='sigResponse123')
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