import requests, json
from urllib.parse import quote

import json
import requests
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


def create_order(payment_method: str, email: str, firstname: str, lastname: str, street: list, city: str, region: str, region_id: int, region_code: str, country_id: str, postcode: str, telephone: str) -> int:
    """
    Creates a new order using the customer's payment method and billing address information, returning the order ID upon successful creation.
    
    Args:
        payment_method (str): The payment method to use for the order
        email (str): Customer's email address
        firstname (str): Customer's first name
        lastname (str): Customer's last name
        street (list): List of street address lines
        city (str): Customer's city
        region (str): Customer's region/state
        region_id (int): ID of the customer's region
        region_code (str): Code of the customer's region
        country_id (str): Customer's country ID
        postcode (str): Customer's postal/zip code
        telephone (str): Customer's telephone number
        
    Returns:
        int: The order ID if successful
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    payload = {
        "paymentMethod": {
            "method": payment_method
        },
        "billing_address": {
            "email": email,
            "region": region,
            "region_id": region_id,
            "region_code": region_code,
            "country_id": country_id,
            "street": street,
            "postcode": postcode,
            "city": city,
            "telephone": telephone,
            "firstname": firstname,
            "lastname": lastname
        }
    }
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information"
    
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = create_order(
        payment_method="banktransfer",
        email="jdoe@example.com",
        firstname="Jane",
        lastname="Doe",
        street=["123 Oak Ave"],
        city="Purchase",
        region="New York",
        region_id=43,
        region_code="NY",
        country_id="US",
        postcode="10577",
        telephone="512-555-1111"
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