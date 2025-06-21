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


def get_order_totals_preview(shipping_carrier_code: str = 'flatrate', shipping_method_code: str = 'flatrate'):
    """
    Calculates and returns a preview of order totals based on specified shipping method.
    
    This function sets the shipping and billing information for the customer's cart 
    and returns the payment methods and order total calculations.
    
    Args:
        shipping_carrier_code (str): The carrier code to use (tablerate or flatrate). Default is 'flatrate'.
        shipping_method_code (str): The shipping method code (bestway, tablerate, or flatrate). Default is 'flatrate'.
        
    Returns:
        Returns a preview of order totals and available payment methods based on the specified shipping carrier and method.
    Example:
        # Get order totals with default shipping method
        totals = get_order_totals_preview()
        
        # Get order totals with tablerate shipping
        totals = get_order_totals_preview('tablerate', 'bestway')
    """
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {get_shopping_customer_auth_token()}'}
    
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
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/mine/shipping-information',
        headers = headers,
        data = json.dumps(payload)
    )
    
    return response.json()

if __name__ == '__main__':
    r = get_order_totals_preview()
    print(json.dumps(r, indent=4))