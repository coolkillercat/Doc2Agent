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

def create_payment_order(cartId=None):
    """
    Create a payment order for guest customer.
    
    Args:
        cartId (str): The ID of the guest cart. Required.
        
    Returns:
        requests.Response: The API response object.
        
    Examples:
        >>> create_payment_order(cartId='12345')
        >>> create_payment_order(cartId='guest123')
        >>> create_payment_order(cartId='cart123')
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{quote(str(cartId))}/payment-information"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "email": "customer@example.com",
        "paymentMethod": {
            "method": "checkmo"
        }
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_payment_order(cartId='12345')
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