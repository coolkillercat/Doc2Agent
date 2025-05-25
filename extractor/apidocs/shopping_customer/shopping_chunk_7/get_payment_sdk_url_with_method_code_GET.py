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

def get_payment_sdk_url_with_method_code(location=None, methodCode=None):
    """
    Get payment SDK URL by location and methodCode.
    
    Args:
        location (str): The location for the payment SDK. Example: 'us'
        methodCode (str): The payment method code. Example: 'paypal'
        
    Returns:
        requests.Response: The API response object
        
    Example:
        >>> get_payment_sdk_url_with_method_code(location='us', methodCode='paypal')
    """
    assert location is not None, 'Missing required parameter: location'
    assert methodCode is not None, 'Missing required parameter: methodCode'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/payment/{methodCode}/sdk-url"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    querystring = {'location': location}
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params=querystring, timeout=50) # in case API can't handle auth headers
        response = response2
    return response

if __name__ == '__main__':
    r = get_payment_sdk_url_with_method_code(location='us', methodCode='paypal')
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