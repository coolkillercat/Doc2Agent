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

def configure_duo_security_provider(tfaToken=None):
    """
    Get the information required to configure duo security provider.
    
    Args:
        tfaToken (str): The two-factor authentication token.
            Example: 'abc123' or 'tfaToken123'
    
    Returns:
        requests.Response: The API response object.
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/tfa/duo_security/configure"
    payload = {'tfaToken': tfaToken}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert tfaToken is not None, 'Missing required parameter: tfaToken'
    
    response = requests.get(url=api_url, headers=headers, params=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = configure_duo_security_provider(tfaToken='abc123')
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