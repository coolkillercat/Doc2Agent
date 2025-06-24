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


def set_shipping_information(shipping_address: dict = None, billing_address: dict = None, shipping_carrier_code: str = 'flatrate', shipping_method_code: str = 'flatrate'):
    """
    Sets shipping and billing information for the current cart, including address details and shipping method, returning available payment methods and order totals.
    
    Args:
        shipping_address (dict, optional): Customer's shipping address details. Defaults to sample address.
        billing_address (dict, optional): Customer's billing address details. Defaults to same as shipping.
        shipping_carrier_code (str, optional): Carrier code ('tablerate' or 'flatrate'). Defaults to 'flatrate'.
        shipping_method_code (str, optional): Method code ('bestway', 'tablerate', or 'flatrate'). Defaults to 'flatrate'.
        
    Returns:
        Response: API response containing payment methods and order totals
        
    Example:
        # Using default values
        response = set_shipping_information()
        
        # Using custom shipping address
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
            "email": "john.smith@example.com",
            "telephone": "213-555-1234"
        }
        response = set_shipping_information(shipping_address=custom_address)
        
        # Using custom carrier and method
        response = set_shipping_information(shipping_carrier_code='flatrate', shipping_method_code='flatrate')
    """
    # Default shipping address if not provided
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
    
    # Default billing address to shipping address if not provided
    if billing_address is None:
        billing_address = shipping_address
    
    # Prepare the request payload
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    # Set up headers
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token()
    }
    
    # Make the API request
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = set_shipping_information()
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