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

def get_apple_pay_config(location=None):
    """
    Get Apple Pay configuration for a specific location.
    
    Args:
        location (str, optional): The location code for which to retrieve Apple Pay configuration.
            If not provided, a default location will be used.
            Example: 'us', 'uk', 'ca'
    
    Returns:
        requests.Response: The API response containing Apple Pay configuration.
    
    Example:
        >>> get_apple_pay_config(location='us')
        <Response [200]>
        >>> get_apple_pay_config()
        <Response [200]>
    """
    # Use default location if none provided
    if location is None:
        location = 'default'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/applepay/config/{quote(location, safe='')}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    
    return response

if __name__ == '__main__':
    r = get_apple_pay_config(location='us')
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