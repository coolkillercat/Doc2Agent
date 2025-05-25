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

def add_gift_card_to_cart(cartId=None, giftCardCode=None, giftCardAmount=None):
    """
    Add a gift card to the cart.
    
    Args:
        cartId (str): The ID of the cart to add the gift card to.
        giftCardCode (str): The code of the gift card.
        giftCardAmount (float): The amount of the gift card.
        
    Returns:
        requests.Response: The response from the API.
        
    Examples:
        >>> add_gift_card_to_cart(cartId='guest123', giftCardCode='GIFT1234', giftCardAmount=50.0)
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert giftCardCode is not None, 'Missing required parameter: giftCardCode'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/{cartId}/giftCards"
    
    payload = {
        'giftCardCode': giftCardCode,
    }
    
    if giftCardAmount is not None:
        payload['giftCardAmount'] = giftCardAmount
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = add_gift_card_to_cart(cartId='guest123', giftCardCode='GIFT1234', giftCardAmount=50.0)
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