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

def vault_payment_nonce(payment=None, billingAddress=None):
    """
    Vault a Payment nonce for a customer. Billing address is optional but advised for Card vaulting.
    
    Args:
        payment (dict): Payment information including payment method code, nonce, and device data.
            Example: {'payment_method_code': 'braintree', 'payment_method_nonce': 'fake-valid-nonce', 'device_data': 'device_data_example'}
        billingAddress (dict, optional): Customer's billing address.
            Example: {'firstname': 'John', 'lastname': 'Doe', 'street': ['123 Main St'], 'city': 'Anytown', 'country_id': 'US', 'postcode': '12345', 'telephone': '555-555-5555'}
    
    Returns:
        requests.Response: The API response object
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information"
    
    assert payment is not None, 'Missing required parameter: payment'
    
    # Convert the set of tuples to a proper payment dictionary if needed
    if isinstance(payment, dict) and any(isinstance(item, tuple) for item in payment.values()):
        payment_data = {}
        for key, value in payment.items():
            if isinstance(value, set):
                for item in value:
                    if isinstance(item, tuple):
                        payment_data[item[0]] = item[1]
            else:
                payment_data[key] = value
        payment = payment_data
    
    payload = {'paymentMethod': payment}
    if billingAddress:
        payload['billingAddress'] = billingAddress
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    payment_data = {'method': 'paypal', 'shopping_chunk_7': 'paypal', 'shopping_chunk_2': 'paypal'}
    r = vault_payment_nonce(payment=payment_data, billingAddress={'firstname': 'John', 'lastname': 'Doe', 'street': ['123 Main St'], 'city': 'Anytown', 'country_id': 'US', 'postcode': '12345', 'telephone': '555-555-5555'})
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