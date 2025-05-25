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

def estimate_shipping_by_address_id(cartId=None, addressId=None):
    """
    Estimate shipping methods by address ID for a cart.
    
    Args:
        cartId (str or int): The ID of the cart. Example: '123'
        addressId (str or int): The ID of the address. Example: 456
        
    Returns:
        requests.Response: The API response object
        
    Example:
        response = estimate_shipping_by_address_id(cartId='123', addressId=456)
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert addressId is not None, 'Missing required parameter: addressId'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/estimate-shipping-methods-by-address-id"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    payload = {'addressId': addressId}
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = estimate_shipping_by_address_id(cartId=123, addressId=456)
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