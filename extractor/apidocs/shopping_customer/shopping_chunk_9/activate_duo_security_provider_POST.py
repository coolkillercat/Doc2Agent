import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get a customer authentication token from the shopping API.
    
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

def activate_duo_security_provider(tfaToken=None, signatureResponse=None):
    """
    Activate the Duo Security provider with the given TFA token and signature response.
    
    Args:
        tfaToken (str): The two-factor authentication token
        signatureResponse (str): The signature response from Duo Security
        
    Returns:
        requests.Response: The response from the API
        
    Example:
        response = activate_duo_security_provider(
            tfaToken='abc123',
            signatureResponse='sigResponse123'
        )
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/tfa/duo_security/activate"
    payload = {'tfaToken': tfaToken, 'signatureResponse': signatureResponse}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert tfaToken is not None, 'Missing required parameter: tfaToken'
    assert signatureResponse is not None, 'Missing required parameter: signatureResponse'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = activate_duo_security_provider(tfaToken='abc123', signatureResponse='sigResponse123')
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