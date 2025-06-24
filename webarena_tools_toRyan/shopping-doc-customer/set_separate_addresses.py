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
    return "Bearer " + response.json()


def set_separate_addresses(shipping_address: dict = None, billing_address: dict = None, shipping_carrier_code: str = 'tablerate', shipping_method_code: str = 'bestway') -> dict:
    """
    Sets different shipping and billing addresses for the current order along with shipping method preferences.
    
    Args:
        shipping_address (dict, optional): Customer shipping address details. Defaults to example address.
        billing_address (dict, optional): Customer billing address details. Defaults to example address.
        shipping_carrier_code (str, optional): Carrier code (tablerate or flatrate). Defaults to 'tablerate'.
        shipping_method_code (str, optional): Method code (bestway, tablerate, or flatrate). Defaults to 'bestway'.
        
    Returns:
        dict: Response from the API containing payment methods and order totals
        
    Example:
        # Using default addresses and shipping methods
        response = set_separate_addresses()
        
        # Using custom addresses
        shipping = {
            "region": "California",
            "region_id": 12,
            "region_code": "CA",
            "country_id": "US",
            "street": ["456 Palm St"],
            "postcode": "90210",
            "city": "Beverly Hills",
            "firstname": "John",
            "lastname": "Smith",
            "email": "john.smith@example.com",
            "telephone": "213-555-1234"
        }
        
        billing = {
            "region": "New York",
            "region_id": 43,
            "region_code": "NY",
            "country_id": "US",
            "street": ["789 Broadway"],
            "postcode": "10001",
            "city": "New York",
            "firstname": "John",
            "lastname": "Smith",
            "email": "john.smith@example.com",
            "telephone": "212-555-6789"
        }
        
        response = set_separate_addresses(
            shipping_address=shipping,
            billing_address=billing,
            shipping_carrier_code="flatrate",
            shipping_method_code="flatrate"
        )
    """
    # Default address if none provided
    default_address = {
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
    
    if shipping_address is None:
        shipping_address = default_address
    
    if billing_address is None:
        billing_address = default_address
    
    # Prepare the payload
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    # Get the auth token
    auth_token = get_shopping_customer_auth_token()
    
    # Set up the headers
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': auth_token
    }
    
    # Make the API call
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = set_separate_addresses() # using default parameters
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