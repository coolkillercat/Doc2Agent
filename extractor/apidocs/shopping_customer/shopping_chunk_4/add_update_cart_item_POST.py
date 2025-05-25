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

def add_update_cart_item(cartId=None, sku=None, qty=1):
    """
    Add or update a cart item in the specified cart.
    
    Args:
        cartId (str): The cart ID to add the item to
        sku (str): The SKU of the product to add
        qty (int): The quantity of the product to add (default: 1)
    
    Returns:
        requests.Response: The API response
    
    Example:
        add_update_cart_item(cartId='12345', sku='24-MB01', qty=2)
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{cartId}/items"
    
    # The cartItem object is required according to the error
    payload = {
        'cartItem': {
            'sku': sku,
            'qty': qty,
            'quote_id': cartId,
            'quoteId': cartId  # Adding the required quoteId field
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    assert cartId is not None, 'Missing required parameter: cartId'
    assert sku is not None, 'Missing required parameter: sku'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = add_update_cart_item(cartId='12345', sku='24-MB01', qty=1)
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