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

def set_payment_information(paymentMethod=None, address=None):
    """
    Set payment information for a specified cart.
    
    Args:
        paymentMethod (dict): The payment method to be used.
            Example: {'method': 'paypal'}
        address (dict): The shipping address information.
            Example: {
                'firstname': 'John',
                'lastname': 'Doe',
                'street': ['123 Main St'],
                'city': 'New York',
                'region_code': 'NY',
                'postcode': '10001',
                'country_id': 'US',
                'telephone': '1234567890'
            }
    
    Returns:
        requests.Response: The API response object
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/set-payment-information"
    
    assert paymentMethod is not None, 'Missing required parameter: paymentMethod'
    assert address is not None, 'Missing required parameter: address'
    
    # Convert set of tuples to proper payment method format if needed
    if isinstance(paymentMethod, set):
        method_value = next(iter(paymentMethod))[1]
        paymentMethod = {'method': method_value}
    
    payload = {
        'paymentMethod': paymentMethod,
        'billingAddress': address,
        'shippingAddress': address
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Sample address
    address = {
        'firstname': 'John',
        'lastname': 'Doe',
        'street': ['123 Main St'],
        'city': 'New York',
        'region_code': 'NY',
        'postcode': '10001',
        'country_id': 'US',
        'telephone': '1234567890'
    }
    
    # Convert the set to a proper payment method
    payment_method_set = {'paymentMethod': {('shopping_chunk_7', 'paypal'), ('shopping_chunk_2', 'paypal')}}
    payment_method = {'method': 'paypal'}
    
    r = set_payment_information(paymentMethod=payment_method, address=address)
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