import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get a customer authentication token from the shopping API.
    
    Returns:
        str: The authentication token for the customer.
        
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

def activate_google_provider(tfaToken=None, otp=None):
    """
    Activate the Google provider for two-factor authentication.
    
    Args:
        tfaToken (str): The two-factor authentication token.
        otp (str): The one-time password.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        response = activate_google_provider(tfaToken='abc123', otp='123456')
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/tfa/google/activate"
    payload = {'tfaToken': tfaToken, 'otp': otp}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert tfaToken is not None, 'Missing required parameter: tfaToken'
    assert otp is not None, 'Missing required parameter: otp'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Extract a single value from the set if it's in that format
    tfaToken_value = next(iter(next(iter(tfaToken))[1] for tfaToken in [{'tfaToken': {('shopping_chunk_9', 'abc123'), ('shopping_chunk_10', 'tfaToken123')}}] if 'tfaToken' in tfaToken), 'abc123')
    r = activate_google_provider(tfaToken=tfaToken_value, otp='123456')
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