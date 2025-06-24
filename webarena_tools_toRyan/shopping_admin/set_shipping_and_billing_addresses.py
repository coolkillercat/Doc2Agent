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


def set_shipping_and_billing_addresses(first_name: str, last_name: str, street: str, city: str, region: str, postcode: str, country_id: str = 'US', telephone: str = '', email: str = '', use_same_address_for_billing: bool = True, billing_address: dict = None, shipping_carrier_code: str = 'flatrate', shipping_method_code: str = 'flatrate'):
    """
    Sets shipping and optionally separate billing information using individual address components, simplifying the checkout process by handling address formatting internally.
    
    Args:
        first_name (str): Customer's first name
        last_name (str): Customer's last name
        street (str): Street address
        city (str): City name
        region (str): State or region name
        postcode (str): Postal or ZIP code
        country_id (str, optional): Country ID. Defaults to 'US'.
        telephone (str, optional): Customer's telephone number
        email (str, optional): Customer's email address
        use_same_address_for_billing (bool, optional): Whether to use the same address for billing. Defaults to True.
        billing_address (dict, optional): Custom billing address if use_same_address_for_billing is False
        shipping_carrier_code (str, optional): Carrier code. Defaults to 'flatrate'.
        shipping_method_code (str, optional): Shipping method code. Defaults to 'flatrate'.
        
    Returns:
        requests.Response: API response
        
    Example:
        response = set_shipping_and_billing_addresses(
            first_name="Jane",
            last_name="Doe",
            street="123 Oak Ave",
            city="Purchase",
            region="New York",
            postcode="10577",
            telephone="512-555-1111",
            email="jdoe@example.com",
            shipping_carrier_code="flatrate",
            shipping_method_code="flatrate"
        )
    """
    # Base URL for the API
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    
    # Endpoint for setting shipping information
    endpoint = "/rest/default/V1/carts/mine/shipping-information"
    
    # Headers for the request
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    # Prepare shipping address
    shipping_address = {
        "region": region,
        "country_id": country_id,
        "street": [street],
        "postcode": postcode,
        "city": city,
        "firstname": first_name,
        "lastname": last_name,
        "telephone": telephone,
        "email": email
    }
    
    # Use shipping address as billing address if specified
    if use_same_address_for_billing:
        billing_address = shipping_address
    
    # Prepare the payload
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    # Make the request
    response = requests.post(
        url=base_url + endpoint,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = set_shipping_and_billing_addresses(
        first_name="Jane",
        last_name="Doe",
        street="123 Oak Ave",
        city="Purchase",
        region="New York",
        postcode="10577",
        telephone="512-555-1111",
        email="jdoe@example.com",
        shipping_carrier_code="flatrate",
        shipping_method_code="flatrate"
    )
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