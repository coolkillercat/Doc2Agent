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

def set_gift_message_for_item(cartId=None, itemId=None, giftMessage=None):
    """
    Set a gift message for a specific item in a cart.
    
    Args:
        cartId: The ID of the cart
        itemId: The ID of the item in the cart
        giftMessage: The gift message to be added to the item
        
    Returns:
        Response object from the API request
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/{cartId}/gift-message/{itemId}"
    payload = {
        'gift_message': {
            'message': giftMessage if giftMessage else "This is a gift for you!"
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_admin_admin_auth_token(),
    }
    assert cartId is not None, 'Missing required parameter: cartId'
    assert itemId is not None, 'Missing required parameter: itemId'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = set_gift_message_for_item(cartId=123, itemId=456, giftMessage="Happy Birthday!")
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