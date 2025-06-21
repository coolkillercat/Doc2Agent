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
    return "Bearer " + response.text.strip('"')


def set_customer_shipping_details(first_name: str, last_name: str, street_address: str, city: str, region: str, region_code: str, postal_code: str, country_id: str, email: str, telephone: str, carrier_code: str = 'tablerate', method_code: str = 'bestway', use_for_billing: bool = True, region_id: int = 43) -> dict:
    """
    Sets shipping and billing information for the customer's cart.
    
    Args:
        first_name (str): Customer's first name
        last_name (str): Customer's last name
        street_address (str): Street address
        city (str): City name
        region (str): Region/state name
        region_code (str): Region/state code
        postal_code (str): Postal/ZIP code
        country_id (str): Country ID (e.g., 'US')
        email (str): Customer's email address
        telephone (str): Customer's telephone number
        carrier_code (str, optional): Shipping carrier code. Defaults to 'tablerate'.
        method_code (str, optional): Shipping method code. Defaults to 'bestway'.
        use_for_billing (bool, optional): Use same address for billing. Defaults to True.
        region_id (int, optional): Region ID. Defaults to 43.
        
    Returns:
        dict: Response from the API with payment methods and order totals
        
    Example:
        response = set_customer_shipping_details(
            first_name="Jane",
            last_name="Doe",
            street_address="123 Oak Ave",
            city="Purchase",
            region="New York",
            region_code="NY",
            postal_code="10577",
            country_id="US",
            email="jdoe@example.com",
            telephone="512-555-1111"
        )
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    # Create shipping address
    shipping_address = {
        "region": region,
        "region_id": region_id,
        "region_code": region_code,
        "country_id": country_id,
        "street": [street_address],
        "postcode": postal_code,
        "city": city,
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "telephone": telephone
    }
    
    # Use the same address for billing if requested
    billing_address = shipping_address.copy() if use_for_billing else None
    
    # Prepare payload
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address if billing_address else shipping_address,
            "shipping_carrier_code": carrier_code,
            "shipping_method_code": method_code
        }
    }
    
    # Make the API request
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = set_customer_shipping_details(
        first_name="Jane",
        last_name="Doe",
        street_address="123 Oak Ave",
        city="Purchase",
        region="New York",
        region_code="NY",
        postal_code="10577",
        country_id="US",
        email="jdoe@example.com",
        telephone="512-555-1111",
        carrier_code="tablerate",
        method_code="bestway"
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