import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get a customer authentication token from the Magento API.
    
    Returns:
        str: The customer authentication token.
        
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

def authenticate_with_onetouch():
    """
    Authenticate using the present OneTouch response and get an admin token.
    
    Returns:
        requests.Response: The response from the OneTouch authentication API.
        
    Example:
        response = authenticate_with_onetouch()
        
    Parameters:
        No parameters required for this function.
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/V1/tfa/provider/authy/authenticate-onetouch"
    payload = {}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token()
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = authenticate_with_onetouch()
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