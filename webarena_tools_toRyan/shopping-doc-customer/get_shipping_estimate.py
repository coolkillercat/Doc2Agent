import requests, json
from urllib.parse import quote
from dataclasses import dataclass

@dataclass
class ShippingAddress:
    """Class to represent shipping address details"""
    region: str
    region_id: int
    region_code: str
    country_id: str
    street: list
    postcode: str
    city: str
    firstname: str
    lastname: str
    customer_id: int
    email: str
    telephone: str
    same_as_billing: int = 1

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


def get_shipping_estimate(address_details: ShippingAddress):
    """
    Provides shipping cost estimates for all available shipping methods.
    
    Args:
        address_details (ShippingAddress): The shipping address details
        
    Returns:
        requests.Response: The API response containing shipping method costs
        
    Example:
        address = ShippingAddress(
            region="New York",
            region_id=43,
            region_code="NY",
            country_id="US",
            street=["123 Oak Ave"],
            postcode="10577",
            city="Purchase",
            firstname="Jane",
            lastname="Doe",
            customer_id=4,
            email="jdoe@example.com",
            telephone="(512) 555-1111"
        )
        response = get_shipping_estimate(address)
    """
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token(),
    }
    
    payload = {
        "address": {
            "region": address_details.region,
            "region_id": address_details.region_id,
            "region_code": address_details.region_code,
            "country_id": address_details.country_id,
            "street": address_details.street,
            "postcode": address_details.postcode,
            "city": address_details.city,
            "firstname": address_details.firstname,
            "lastname": address_details.lastname,
            "customer_id": address_details.customer_id,
            "email": address_details.email,
            "telephone": address_details.telephone,
            "same_as_billing": address_details.same_as_billing
        }
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/estimate-shipping-methods',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    # Create a sample shipping address
    sample_address = ShippingAddress(
        region="New York",
        region_id=43,
        region_code="NY",
        country_id="US",
        street=["123 Oak Ave"],
        postcode="10577",
        city="Purchase",
        firstname="Jane",
        lastname="Doe",
        customer_id=4,
        email="jdoe@example.com",
        telephone="(512) 555-1111"
    )
    
    r = get_shipping_estimate(sample_address)
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