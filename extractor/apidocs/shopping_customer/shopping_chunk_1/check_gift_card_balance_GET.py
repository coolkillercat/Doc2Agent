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

def check_gift_card_balance(cartId=None, giftCardCode=None):
    """
    Check gift card balance if added to the cart.
    
    Args:
        cartId (str): The ID of the cart to check the gift card balance for.
            Example: 'guest123', 'cart123', '12345'
        giftCardCode (str): The gift card code to check the balance for.
            Example: 'GIFT1234', 'GIFT123'
    
    Returns:
        requests.Response: The API response object.
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert giftCardCode is not None, 'Missing required parameter: giftCardCode'
    
    headers = {
        "Content-Type": "application/json"
    }
    
    # Try guest cart endpoint first
    guest_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{quote(cartId, safe='')}/giftCards/{quote(giftCardCode, safe='')}"
    response = requests.get(url=guest_url, headers=headers, timeout=50, verify=False)
    
    # If guest cart fails, try authenticated cart
    if response.status_code != 200:
        auth_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/giftCards/{quote(giftCardCode, safe='')}"
        headers["Authorization"] = "Bearer " + get_shopping_customer_auth_token()
        response = requests.get(url=auth_url, headers=headers, timeout=50, verify=False)
    
    return response

if __name__ == '__main__':
    r = check_gift_card_balance(cartId='guest123', giftCardCode='GIFT1234')
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