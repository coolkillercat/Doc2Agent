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


def submit_payment_information(payment_method_code: str, billing_address: dict) -> requests.Response:
    """
    Submits payment information with the specified payment method code and complete billing address, finalizing the order and returning the order ID.
    
    Args:
        payment_method_code (str): The payment method code (e.g., "banktransfer")
        billing_address (dict): Dictionary containing billing address information
        
    Returns:
        requests.Response: Response from the API containing the order ID
        
    Example:
        billing_info = {
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
        response = submit_payment_information("banktransfer", billing_info)
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    payload = {
        "paymentMethod": {
            "method": payment_method_code
        },
        "billing_address": billing_address
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    billing_address = {
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
    
    r = submit_payment_information("banktransfer", billing_address)
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