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

def estimate_shipping_methods(cartId=None):
    """
    Estimate shipping by address and return list of available shipping methods.
    
    Args:
        cartId (str): The ID of the cart to estimate shipping for.
            Example: '12345', 'cart123', 'guest123'
    
    Returns:
        requests.Response: The API response object.
    
    Raises:
        AssertionError: If cartId is not provided.
    
    Example:
        >>> estimate_shipping_methods(cartId='12345')
        >>> estimate_shipping_methods(cartId='cart123')
        >>> estimate_shipping_methods(cartId='guest123')
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/{cartId}/estimate-shipping-methods"
    
    payload = {
        'address': {
            'region': 'New York',
            'region_id': 43,
            'country_id': 'US',
            'postcode': '10001'
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = estimate_shipping_methods(cartId='12345')
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