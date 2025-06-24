import requests, json
from urllib.parse import quote
from dataclasses import dataclass

@dataclass
class ShippingAddress:
    """Class for storing shipping address information"""
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
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return "Bearer " + response.json()


def get_shipping_options(address: ShippingAddress):
    """
    Get shipping cost estimates for a given shipping address.
    
    Args:
        address (ShippingAddress): Shipping address information
        
    Returns:
        Returns available shipping method options and their associated costs for a specified delivery address.
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
        response = get_shipping_options(address)
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    payload = {
        "address": {
            "region": address.region,
            "region_id": address.region_id,
            "region_code": address.region_code,
            "country_id": address.country_id,
            "street": address.street,
            "postcode": address.postcode,
            "city": address.city,
            "firstname": address.firstname,
            "lastname": address.lastname,
            "customer_id": address.customer_id,
            "email": address.email,
            "telephone": address.telephone,
            "same_as_billing": address.same_as_billing
        }
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/mine/estimate-shipping-methods',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    # Create a sample shipping address
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
    
    r = get_shipping_options(address)
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