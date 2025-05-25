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

def estimate_shipping_methods(cartId=None, address=None):
    """
    Estimate shipping by address and return list of available shipping methods.
    
    Args:
        cartId (str): The ID of the cart to estimate shipping for.
            Examples: '123', 'cart123', 'guest123', '12345'
        address (dict): The shipping address information.
            Example: {
                'region': 'New York',
                'region_id': 43,
                'region_code': 'NY',
                'country_id': 'US',
                'street': ['123 Main St'],
                'postcode': '10001',
                'city': 'New York',
                'firstname': 'John',
                'lastname': 'Doe',
                'customer_id': 1,
                'email': 'sample@example.com',
                'telephone': '(555) 555-5555',
                'same_as_billing': 1
            }
    
    Returns:
        requests.Response: The API response object containing shipping methods.
    
    Raises:
        AssertionError: If cartId is not provided.
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    
    if address is None:
        address = {
            'region': 'New York',
            'region_id': 43,
            'region_code': 'NY',
            'country_id': 'US',
            'street': ['123 Main St'],
            'postcode': '10001',
            'city': 'New York',
            'firstname': 'John',
            'lastname': 'Doe',
            'customer_id': 1,
            'email': 'sample@example.com',
            'telephone': '(555) 555-5555',
            'same_as_billing': 1
        }
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/{cartId}/estimate-shipping-methods"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=address, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = estimate_shipping_methods(cartId='123')
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