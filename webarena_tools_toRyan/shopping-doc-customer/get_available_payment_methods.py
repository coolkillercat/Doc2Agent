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
    token = response.json()
    if isinstance(token, str):
        return "Bearer " + token.strip('"')
    return "Bearer " + token


def set_shipping_information(shipping_address=None, billing_address=None, carrier_code="flatrate", method_code="flatrate"):
    """
    Sets shipping and billing information for the customer's cart and retrieves available payment methods.
    
    This function sends a POST request to set shipping and billing addresses and shipping method, 
    then returns the response containing payment methods and order totals.
    
    Args:
        shipping_address (dict, optional): Customer's shipping address. Defaults to a sample address.
        billing_address (dict, optional): Customer's billing address. Defaults to shipping address if None.
        carrier_code (str, optional): Shipping carrier code. Defaults to "flatrate".
        method_code (str, optional): Shipping method code. Defaults to "flatrate".
    
    Returns:
        dict: Response containing payment methods and order totals
        
    Example:
        # Using default sample address
        payment_info = set_shipping_information()
        
        # Using custom address
        custom_address = {
            "region": "California",
            "region_id": 12,
            "region_code": "CA",
            "country_id": "US",
            "street": ["456 Palm St"],
            "postcode": "90210",
            "city": "Beverly Hills",
            "firstname": "John",
            "lastname": "Smith",
            "email": "jsmith@example.com",
            "telephone": "213-555-1234"
        }
        payment_info = set_shipping_information(shipping_address=custom_address)
        
        # Using tablerate carrier with bestway method
        payment_info = set_shipping_information(carrier_code="tablerate", method_code="bestway")
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    # Default shipping address if none provided
    if shipping_address is None:
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
    
    # Use shipping address as billing address if none provided
    if billing_address is None:
        billing_address = shipping_address
    
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": carrier_code,
            "shipping_method_code": method_code
        }
    }
    
    response = requests.post(
        'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response.json()


if __name__ == '__main__':
    r = set_shipping_information() 
    print(json.dumps(r, indent=4))