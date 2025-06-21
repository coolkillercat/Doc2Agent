import requests
import json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get customer authentication token from the API.
    
    Returns:
        str: Authentication token for the customer
        
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def set_shipping_information(shipping_address, billing_address=None, shipping_carrier_code="flatrate", shipping_method_code="flatrate"):
    """
    Sets shipping and billing information for the customer's cart.
    
    Args:
        shipping_address (dict): Customer's shipping address information
        billing_address (dict, optional): Customer's billing address information. If None, shipping address will be used.
        shipping_carrier_code (str, optional): Carrier code (tablerate or flatrate). Defaults to "flatrate".
        shipping_method_code (str, optional): Method code (bestway, tablerate, or flatrate). Defaults to "flatrate".
        
    Returns:
        Returns available payment methods and order totals after setting shipping information for a customer's cart.
    Example:
        shipping_address = {
            "region": "New York",
            "region_id": 43,
            "region_code": "NY",
            "country_id": "US",
            "street": ["123 Oak Ave"],
            "postcode": "10577",
            "city": "Purchase",
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jdoe@example.com",
            "telephone": "512-555-1111"
        }
        response = set_shipping_information(shipping_address)
    """
    if billing_address is None:
        billing_address = shipping_address
    
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {get_shopping_customer_auth_token()}"
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    # Create sample shipping address
    shipping_address = {
        "region": "New York",
        "region_id": 43,
        "region_code": "NY",
        "country_id": "US",
        "street": ["123 Oak Ave"],
        "postcode": "10577",
        "city": "Purchase",
        "firstname": "Jane",
        "lastname": "Doe",
        "email": "jdoe@example.com",
        "telephone": "512-555-1111"
    }
    
    r = set_shipping_information(shipping_address)
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))