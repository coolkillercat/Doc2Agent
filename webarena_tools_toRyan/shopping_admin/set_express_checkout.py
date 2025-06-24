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


def set_express_checkout(first_name: str, last_name: str, street: str, city: str, region: str, postcode: str, country_id: str = 'US', telephone: str = '512-555-1111', email: str = 'jdoe@example.com', shipping_carrier_code: str = 'flatrate', shipping_method_code: str = 'flatrate'):
    """
    Sets shipping and billing information for the cart and returns payment options and order totals.
    
    Args:
        first_name (str): Customer's first name
        last_name (str): Customer's last name
        street (str): Street address
        city (str): City name
        region (str): Region/state name
        postcode (str): Postal/zip code
        country_id (str, optional): Country ID. Defaults to 'US'.
        telephone (str, optional): Customer's telephone number. Defaults to '512-555-1111'.
        email (str, optional): Customer's email address. Defaults to 'jdoe@example.com'.
        shipping_carrier_code (str, optional): Carrier code. Defaults to 'flatrate'.
        shipping_method_code (str, optional): Shipping method code. Defaults to 'flatrate'.
    
    Returns:
        requests.Response: API response containing payment methods and totals
        
    Example:
        response = set_express_checkout(
            first_name="Jane",
            last_name="Doe",
            street="123 Oak Ave",
            city="Purchase",
            region="New York",
            postcode="10577",
            shipping_carrier_code="flatrate",
            shipping_method_code="flatrate"
        )
    """
    # Determine region_id and region_code based on region
    region_mapping = {
        "New York": {"id": 43, "code": "NY"},
        "California": {"id": 12, "code": "CA"},
        "Texas": {"id": 57, "code": "TX"}
    }
    
    region_info = region_mapping.get(region, {"id": 0, "code": ""})
    region_id = region_info["id"]
    region_code = region_info["code"]
    
    # Prepare the address information
    address = {
        "region": region,
        "region_id": region_id,
        "region_code": region_code,
        "country_id": country_id,
        "street": [street],
        "postcode": postcode,
        "city": city,
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "telephone": telephone
    }
    
    # Prepare the request payload
    payload = {
        "addressInformation": {
            "shipping_address": address,
            "billing_address": address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    # Make the API request
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token()
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response


if __name__ == '__main__':
    r = set_express_checkout(
        first_name="Jane",
        last_name="Doe",
        street="123 Oak Ave",
        city="Purchase",
        region="New York",
        postcode="10577",
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