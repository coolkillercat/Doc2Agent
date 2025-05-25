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

def get_gift_message_for_item(cartId=None, itemId=None):
    """
    Return the gift message for a specified item in a specified shopping cart.
    
    Args:
        cartId (str): The ID of the shopping cart. Example: '12345'
        itemId (int or str): The ID of the item in the cart. Example: 1
    
    Returns:
        requests.Response: The API response containing gift message information
        
    Example:
        >>> get_gift_message_for_item(cartId='12345', itemId=1)
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert itemId is not None, 'Missing required parameter: itemId'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/gift-message/{quote(str(itemId), safe='')}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        # Try alternative endpoint for guest carts
        api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{quote(str(cartId), safe='')}/gift-message/{quote(str(itemId), safe='')}"
        response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_gift_message_for_item(cartId='12345', itemId=1)
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