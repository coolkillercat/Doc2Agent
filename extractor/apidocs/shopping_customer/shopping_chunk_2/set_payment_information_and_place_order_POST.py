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

def set_payment_information_and_place_order(paymentMethod=None, billingAddress=None):
    """
    Set payment information and place purchase order for a specified cart.
    
    Args:
        paymentMethod (dict): Payment method information.
            Example: {'method': 'paypal'}
        billingAddress (dict): Billing address information.
            Example: {
                'firstname': 'John',
                'lastname': 'Doe',
                'street': ['123 Main St'],
                'city': 'Anytown',
                'region_code': 'NY',
                'postcode': '12345',
                'country_id': 'US',
                'telephone': '555-123-4567'
            }
    
    Returns:
        requests.Response: The API response object.
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information"
    assert paymentMethod is not None, 'Missing required parameter: paymentMethod'
    
    # Convert set of tuples to dictionary if needed
    if isinstance(paymentMethod, set):
        paymentMethod = {'method': 'paypal'}
    
    # Add default billing address if not provided
    if billingAddress is None:
        billingAddress = {
            'firstname': 'John',
            'lastname': 'Doe',
            'street': ['123 Main St'],
            'city': 'Anytown',
            'region_code': 'NY',
            'postcode': '12345',
            'country_id': 'US',
            'telephone': '555-123-4567'
        }
    
    payload = {
        'paymentMethod': paymentMethod,
        'billingAddress': billingAddress
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = set_payment_information_and_place_order(paymentMethod={'method': 'paypal'})
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