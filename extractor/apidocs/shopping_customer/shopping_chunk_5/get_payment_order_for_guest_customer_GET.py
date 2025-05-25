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

def get_payment_order_for_guest_customer(cartId=None, id=None):
    """
    Retrieve payment order details for a guest customer.
    
    Args:
        cartId (str): The ID of the guest cart. Required.
        id (str): The ID of the payment order. Required.
        
    Returns:
        requests.Response: The API response object.
        
    Examples:
        >>> get_payment_order_for_guest_customer(cartId='12345', id='67890')
        >>> get_payment_order_for_guest_customer(cartId='cart123', id='order456')
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    assert id is not None, 'Missing required parameter: id'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{quote(str(cartId), safe='')}/payment-information/{quote(str(id), safe='')}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        # Try without headers in case API doesn't require them for guest carts
        response2 = requests.get(url=api_url, timeout=50, verify=False)
        response = response2
    return response

if __name__ == '__main__':
    r = get_payment_order_for_guest_customer(cartId='12345', id='67890')
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