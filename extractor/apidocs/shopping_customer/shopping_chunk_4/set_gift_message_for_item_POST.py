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

def set_gift_message_for_item(cartId=None, itemId=None, message=None, sender=None, recipient=None):
    """
    Set the gift message for a specified item in a specified shopping cart.
    
    Args:
        cartId (str): The cart ID
        itemId (int): The item ID
        message (str): The gift message content
        sender (str): The name of the sender
        recipient (str): The name of the recipient
        
    Returns:
        requests.Response: The API response
        
    Example:
        set_gift_message_for_item(
            cartId='12345',
            itemId=1,
            message='Happy Birthday!',
            sender='John',
            recipient='Jane'
        )
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert itemId is not None, 'Missing required parameter: itemId'
    assert message is not None, 'Missing required parameter: message'
    
    # Use customer carts endpoint instead of guest carts since we're using authentication
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/gift-message/{itemId}"
    
    payload = {
        'gift_message': {
            'message': message,
            'sender': sender or '',
            'recipient': recipient or ''
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = set_gift_message_for_item(cartId='12345', itemId=1, message="Happy Birthday!", sender="John", recipient="Jane")
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