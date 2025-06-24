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


def estimate_shipping_costs(region: str, region_id: int, region_code: str, country_id: str, street: list, postcode: str, city: str, firstname: str, lastname: str, customer_id: int, email: str, telephone: str, same_as_billing: bool = True):
    """
    Calculates shipping costs for all available shipping methods based on a customer's shipping address.
    
    Args:
        region (str): State/province name
        region_id (int): Region ID
        region_code (str): Region code (e.g. 'NY')
        country_id (str): Country ID (e.g. 'US')
        street (list): Street address lines
        postcode (str): Postal code
        city (str): City name
        firstname (str): Customer's first name
        lastname (str): Customer's last name
        customer_id (int): Customer ID
        email (str): Customer's email
        telephone (str): Customer's phone number
        same_as_billing (bool, optional): Whether shipping address is same as billing. Defaults to True.
        
    Returns:
        requests.Response: Response from the API containing shipping cost estimates
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    payload = {
        "address": {
            "region": region,
            "region_id": region_id,
            "region_code": region_code,
            "country_id": country_id,
            "street": street,
            "postcode": postcode,
            "city": city,
            "firstname": firstname,
            "lastname": lastname,
            "customer_id": customer_id,
            "email": email,
            "telephone": telephone,
            "same_as_billing": 1 if same_as_billing else 0
        }
    }
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/estimate-shipping-methods"
    
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = estimate_shipping_costs(
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
        telephone="(512) 555-1111",
        same_as_billing=True
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