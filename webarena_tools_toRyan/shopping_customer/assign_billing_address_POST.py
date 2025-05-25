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

def assign_billing_address(cartId=None, address=None):
    """
    Assigns a specified billing address to a specified cart.
    
    Args:
        cartId (str or int): The ID of the cart to assign the billing address to.
            Example: 123, '12345', 'cart123', 'guest123'
        address (dict): The billing address information to assign to the cart.
            Example: {
                'firstname': 'John',
                'lastname': 'Doe',
                'street': ['123 Main St'],
                'city': 'New York',
                'region_code': 'NY',
                'postcode': '10001',
                'country_id': 'US',
                'telephone': '1234567890'
            }
    
    Returns:
        requests.Response: The response from the API.
    """
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
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/billing-address"
    
    payload = {
        'address': address
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = assign_billing_address(cartId=123)
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