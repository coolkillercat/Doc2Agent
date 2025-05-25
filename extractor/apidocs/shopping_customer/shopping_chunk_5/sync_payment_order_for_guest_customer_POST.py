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

def sync_payment_order_for_guest_customer(cartId=None, id=None, email=None, paymentMethod=None):
    """
    Synchronize payment order for a guest customer.
    
    Args:
        cartId (str): The ID of the guest cart. Example: '12345'
        id (str): The ID of the payment order. Example: '67890'
        email (str): The email of the guest customer. Example: 'guest@example.com'
        paymentMethod (dict): The payment method information. Example: {'method': 'checkmo'}
        
    Returns:
        requests.Response: The API response object
        
    Example:
        >>> sync_payment_order_for_guest_customer(
        ...     cartId='12345', 
        ...     id='67890', 
        ...     email='guest@example.com', 
        ...     paymentMethod={'method': 'checkmo'}
        ... )
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{cartId}/payment-information"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        'cartId': cartId,
        'email': email or 'guest@example.com',
        'paymentMethod': paymentMethod or {'method': 'checkmo'}
    }
    
    if id is not None:
        payload['id'] = id
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = sync_payment_order_for_guest_customer(cartId='12345', id='67890', email='guest@example.com', paymentMethod={'method': 'checkmo'})
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