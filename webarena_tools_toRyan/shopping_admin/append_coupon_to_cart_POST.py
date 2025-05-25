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

def append_coupon_to_cart(cartId=None, couponCode=None):
    """
    Append a coupon to a cart.
    
    Args:
        cartId (str or int): The ID of the cart to which the coupon will be appended.
        couponCode (str): The coupon code to append to the cart.
        
    Returns:
        requests.Response: The response from the API.
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert couponCode is not None, 'Missing required parameter: couponCode'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/{cartId}/coupons/{couponCode}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_admin_admin_auth_token(),
    }
    
    response = requests.put(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = append_coupon_to_cart(cartId=67890, couponCode="DISCOUNT10")
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