import requests, json
from urllib.parse import quote

import json
import requests
def get_shopping_customer_auth_token():
    """
    Get customer authentication token from the API.
    
    Returns:
        str: Authentication token for the customer
        
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return "Bearer " + response.json()


def complete_checkout(payment_method: str = "banktransfer", billing_details: dict = None) -> requests.Response:
    """
    Completes the checkout process by submitting the payment method and billing details, creating an order and returning the order ID.
    
    Args:
        payment_method (str): The payment method to use. Default is "banktransfer".
        billing_details (dict): Dictionary containing billing address details. If None, default details are used.
        
    Returns:
        requests.Response: The response from the API containing the order ID
    """
    if billing_details is None:
        billing_details = {
            "email": "jdoe@example.com",
            "region": "New York",
            "region_id": 43,
            "region_code": "NY",
            "country_id": "US",
            "street": ["123 Oak Ave"],
            "postcode": "10577",
            "city": "Purchase",
            "telephone": "512-555-1111",
            "firstname": "Jane",
            "lastname": "Doe"
        }
    
    payload = {
        "paymentMethod": {
            "method": payment_method
        },
        "billing_address": billing_details
    }
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token()
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = complete_checkout()  # Using default parameters
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