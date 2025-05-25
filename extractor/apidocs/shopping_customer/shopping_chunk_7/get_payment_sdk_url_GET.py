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

def get_payment_sdk_url(location=None):
    """
    Get payment SDK URL by location.
    
    Args:
        location (str): The location code for which to get the payment SDK URL.
                        Example: 'us', 'uk', 'eu'
    
    Returns:
        requests.Response: The API response containing payment SDK URL information.
    
    Raises:
        AssertionError: If the required location parameter is not provided.
    
    Example:
        >>> get_payment_sdk_url(location='us')
        <Response [200]>
    """
    assert location is not None, 'Missing required parameter: location'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/payment/sdk/url"
    querystring = {'location': location}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
        response = response2
    return response

if __name__ == '__main__':
    r = get_payment_sdk_url(location='us')
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