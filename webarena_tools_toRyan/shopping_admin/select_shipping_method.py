import requests
import json

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
    return response.json()


def set_shipping_information(shipping_address=None, billing_address=None, carrier_code="flatrate", method_code="flatrate"):
    """
    Sets shipping and billing information for the current cart.
    
    Args:
        shipping_address (dict, optional): The shipping address information. If None, a default address will be used.
        billing_address (dict, optional): The billing address information. If None, shipping_address will be used.
        carrier_code (str, optional): The carrier code (tablerate or flatrate). Defaults to "flatrate".
        method_code (str, optional): The shipping method code (bestway, tablerate, or flatrate). Defaults to "flatrate".
        
    Returns:
        dict: The API response containing payment methods and order totals
        
    Example:
        # Example address information
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
        
        # Using the same address for billing
        billing_address = shipping_address.copy()
        
        # Call the function with the flatrate carrier and flatrate method
        result = set_shipping_information(
            shipping_address=shipping_address,
            billing_address=billing_address,
            carrier_code="flatrate",
            method_code="flatrate"
        )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    
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
    
    # Use shipping address for billing if none provided
    if billing_address is None:
        billing_address = shipping_address.copy()
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_shopping_customer_auth_token()}'
    }
    
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": carrier_code,
            "shipping_method_code": method_code
        }
    }
    
    response = requests.post(
        url=f'{base_url}/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response.json()


if __name__ == '__main__':
    # Example address information
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
    
    # Using the same address for billing
    billing_address = shipping_address.copy()
    
    # Call the function with the flatrate carrier and flatrate method
    r = set_shipping_information(
        shipping_address=shipping_address,
        billing_address=billing_address,
        carrier_code="flatrate",
        method_code="flatrate"
    )
    
    print(json.dumps(r, indent=4))