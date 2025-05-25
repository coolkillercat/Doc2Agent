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

def get_smart_buttons_config(location=None):
    """
    Get Smart Buttons Config from the API.
    
    Args:
        location (str): The location for which to get smart buttons configuration.
                        Example: 'us'
    
    Returns:
        requests.Response: The API response object.
    
    Raises:
        AssertionError: If the required location parameter is missing.
    
    Example:
        >>> get_smart_buttons_config(location='us')
    """
    assert location is not None, 'Missing required parameter: location'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/payment-config/smart-buttons/{quote(location, safe='')}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50, verify=False)
        response = response2
    return response

if __name__ == '__main__':
    r = get_smart_buttons_config(location='us')
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