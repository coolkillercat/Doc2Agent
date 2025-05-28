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

def get_coupon_information_for_cart(cartId=None):
    """
    Return information for a coupon in a specified cart.
    
    Args:
        cartId (str): The ID of the cart to retrieve coupon information for.
            Example: 'cart123', 'guest123', '12345', '123'
    
    Returns:
        requests.Response: The API response containing coupon information.
    
    Raises:
        AssertionError: If cartId is not provided.
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    
    # Try customer cart endpoint first
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/coupons"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    
    if response.status_code != 200:
        # Try guest cart endpoint
        guest_api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{quote(str(cartId), safe='')}/coupons"
        response = requests.get(url=guest_api_url, headers=headers, timeout=50, verify=False)
    
    return response

if __name__ == '__main__':
    r = get_coupon_information_for_cart(cartId='cart123')
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