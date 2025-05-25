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

def create_payment_order(methodCode=None, paymentSource=None, location=None, vaultIntent=None):
    """
    Create a payment order for logged in customer.
    
    Args:
        methodCode (str): The payment method code. Required.
        paymentSource (dict): The payment source information. Required.
        location (str): The location for the payment. Required.
        vaultIntent (bool, optional): Whether to vault the payment method.
    
    Returns:
        requests.Response: The API response object.
    
    Example:
        >>> create_payment_order(
        ...     methodCode='paypal',
        ...     paymentSource={'shopping_chunk_2': 'credit_card'},
        ...     location='US',
        ...     vaultIntent=True
        ... )
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information"
    payload = {
        'paymentMethod': {
            'method': methodCode,
            'additional_data': paymentSource
        },
        'location': location
    }
    
    if vaultIntent is not None:
        payload['vaultIntent'] = vaultIntent
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert methodCode is not None, 'Missing required parameter: methodCode'
    assert paymentSource is not None, 'Missing required parameter: paymentSource'
    assert location is not None, 'Missing required parameter: location'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_payment_order(methodCode='paypal', paymentSource={'shopping_chunk_2': 'credit_card'}, location='US', vaultIntent=True)
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