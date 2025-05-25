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

def set_gift_message_for_order(cartId=None, giftMessage=None, sender=None, recipient=None):
    """
    Set the gift message for an entire order.
    
    Args:
        cartId (str): The cart ID for the order.
        giftMessage (str): The gift message content.
        sender (str, optional): The name of the sender.
        recipient (str, optional): The name of the recipient.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        set_gift_message_for_order(
            cartId='12345',
            giftMessage='Happy Birthday!',
            sender='John',
            recipient='Jane'
        )
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert giftMessage is not None, 'Missing required parameter: giftMessage'
    
    # Use the customer cart endpoint instead of guest cart
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/gift-message"
    
    payload = {
        'gift_message': {
            'message': giftMessage
        }
    }
    
    if sender is not None:
        payload['gift_message']['sender'] = sender
    
    if recipient is not None:
        payload['gift_message']['recipient'] = recipient
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = set_gift_message_for_order(cartId='12345', giftMessage='Happy Birthday!', sender='John', recipient='Jane')
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