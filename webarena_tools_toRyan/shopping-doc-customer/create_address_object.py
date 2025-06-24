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
    return response.json()


def create_address_object(first_name: str, last_name: str, street: str, city: str, region: str, 
                          region_code: str, region_id: int, postal_code: str, country_id: str, 
                          email: str, telephone: str, shipping_carrier_code: str = "tablerate", 
                          shipping_method_code: str = "bestway") -> requests.Response:
    """
    Set shipping and billing information for the customer's cart.

    Args:
        first_name (str): Customer's first name
        last_name (str): Customer's last name
        street (str): Street address
        city (str): City name
        region (str): Region/state name
        region_code (str): Region/state code
        region_id (int): Region/state ID
        postal_code (str): Postal/ZIP code
        country_id (str): Country ID (e.g., "US")
        email (str): Customer's email address
        telephone (str): Customer's telephone number
        shipping_carrier_code (str, optional): Carrier code. Defaults to "tablerate".
        shipping_method_code (str, optional): Shipping method code. Defaults to "bestway".

    Returns:
        requests.Response: API response containing payment methods and order totals
        
    Example:
        response = create_address_object(
            first_name="Jane",
            last_name="Doe",
            street="123 Oak Ave",
            city="Purchase",
            region="New York",
            region_code="NY",
            region_id=43,
            postal_code="10577",
            country_id="US",
            email="jdoe@example.com",
            telephone="512-555-1111"
        )
    """
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f"Bearer {get_shopping_customer_auth_token()}"
    }
    
    # Create the address object that will be used for both shipping and billing
    address = {
        "region": region,
        "region_id": region_id,
        "region_code": region_code,
        "country_id": country_id,
        "street": [street],
        "postcode": postal_code,
        "city": city,
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "telephone": telephone
    }
    
    # Create the payload
    payload = {
        "addressInformation": {
            "shipping_address": address,
            "billing_address": address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    # Make the API request
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response


if __name__ == '__main__':
    # Test the function with sample parameters
    r = create_address_object(
        first_name="Jane",
        last_name="Doe",
        street="123 Oak Ave",
        city="Purchase",
        region="New York",
        region_code="NY",
        region_id=43,
        postal_code="10577",
        country_id="US",
        email="jdoe@example.com",
        telephone="512-555-1111"
    )
    
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