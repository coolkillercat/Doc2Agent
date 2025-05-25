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

def set_shipping_information(cartId=None, address=None, shipping_method_code=None, shipping_carrier_code=None):
    """
    Set shipping information for a specified cart.
    
    Args:
        cartId (str or int): The ID of the cart to set shipping information for.
        address (dict, optional): The shipping address information. Default is a sample address.
        shipping_method_code (str, optional): The shipping method code. Default is 'flatrate'.
        shipping_carrier_code (str, optional): The shipping carrier code. Default is 'flatrate'.
    
    Returns:
        requests.Response: The API response object.
    
    Example:
        >>> set_shipping_information(cartId=123)
        >>> set_shipping_information(
        ...     cartId='12345',
        ...     address={
        ...         'firstname': 'John',
        ...         'lastname': 'Doe',
        ...         'street': ['123 Main St'],
        ...         'city': 'New York',
        ...         'region_code': 'NY',
        ...         'postcode': '10001',
        ...         'country_id': 'US',
        ...         'telephone': '1234567890'
        ...     },
        ...     shipping_method_code='flatrate',
        ...     shipping_carrier_code='flatrate'
        ... )
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/{cartId}/shipping-information"
    
    assert cartId is not None, 'Missing required parameter: cartId'
    
    if address is None:
        address = {
            'firstname': 'John',
            'lastname': 'Doe',
            'street': ['123 Main St'],
            'city': 'New York',
            'region_code': 'NY',
            'postcode': '10001',
            'country_id': 'US',
            'telephone': '1234567890'
        }
    
    if shipping_method_code is None:
        shipping_method_code = 'flatrate'
    
    if shipping_carrier_code is None:
        shipping_carrier_code = 'flatrate'
    
    payload = {
        'addressInformation': {
            'shipping_address': address,
            'shipping_method_code': shipping_method_code,
            'shipping_carrier_code': shipping_carrier_code
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = set_shipping_information(cartId=123)
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