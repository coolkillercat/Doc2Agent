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


def update_shipping_method(carrier_code: str, method_code: str) -> dict:
    """
    Updates only the shipping method for an existing cart that already has address information, 
    returning updated totals and payment options.
    
    Args:
        carrier_code (str): The carrier code ('tablerate' or 'flatrate')
        method_code (str): The method code ('bestway', 'tablerate', or 'flatrate')
    
    Returns:
        dict: The response from the API containing payment methods and order totals
        
    Example:
        response = update_shipping_method("tablerate", "bestway")
        response = update_shipping_method("flatrate", "flatrate")
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = "/rest/default/V1/carts/mine/shipping-information"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token()
    }
    
    # Default shipping and billing address data
    payload = {
        "addressInformation": {
            "shipping_address": {
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
            },
            "billing_address": {
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
            },
            "shipping_carrier_code": carrier_code,
            "shipping_method_code": method_code
        }
    }
    
    response = requests.post(
        url=base_url + endpoint,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response.json()


if __name__ == '__main__':
    r = update_shipping_method("tablerate", "bestway")
    r_json = None
    try:
        r_json = r
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))