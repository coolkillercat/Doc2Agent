import requests, json
from urllib.parse import quote

def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url=f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={
            'content-type': 'application/json'
        },
        data=json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return response.json()

def add_shipping_information(cartId=None):
    """
    Add shipping information to a cart.
    
    Args:
        cartId: The ID of the cart to add shipping information to.
        
    Returns:
        Response object from the API call.
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/{cartId}/shipping-information"
    
    payload = {
        'addressInformation': {
            'shipping_address': {
                'firstname': 'John',
                'lastname': 'Doe',
                'street': ['123 Main St'],
                'city': 'Anytown',
                'region': 'CA',
                'region_id': 12,
                'postcode': '12345',
                'country_id': 'US',
                'telephone': '555-1234'
            },
            'billing_address': {
                'firstname': 'John',
                'lastname': 'Doe',
                'street': ['123 Main St'],
                'city': 'Anytown',
                'region': 'CA',
                'region_id': 12,
                'postcode': '12345',
                'country_id': 'US',
                'telephone': '555-1234'
            },
            'shipping_method_code': 'flatrate',
            'shipping_carrier_code': 'flatrate'
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_admin_admin_auth_token(),
    }
    assert cartId is not None, 'Missing required parameter: cartId'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = add_shipping_information(cartId=123)
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