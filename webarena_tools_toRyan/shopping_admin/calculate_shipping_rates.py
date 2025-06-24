import requests, json
from urllib.parse import quote
from dataclasses import dataclass

@dataclass
class CustomerInfo:
    """Customer information for shipping calculation"""
    firstname: str = "Jane"
    lastname: str = "Doe" 
    email: str = "jdoe@example.com"
    telephone: str = "(512) 555-1111"
    customer_id: int = None

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


def calculate_shipping_rates(city: str, region: str, postcode: str, country_id: str, street_address: str, customer_info: CustomerInfo = None):
    """
    Calculate shipping costs for different shipping methods.
    
    Args:
        city (str): City name for shipping address
        region (str): Region/state name for shipping address
        postcode (str): Postal code for shipping address
        country_id (str): Country ID (e.g., 'US')
        street_address (str): Street address for shipping
        customer_info (CustomerInfo, optional): Customer details. Defaults to None.
        
    Returns:
        requests.Response: Response from the API containing shipping rates
        
    Example:
        response = calculate_shipping_rates(
            city="Purchase", 
            region="New York", 
            postcode="10577", 
            country_id="US", 
            street_address="123 Oak Ave"
        )
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    # Prepare the address payload
    address = {
        "region": region,
        "country_id": country_id,
        "street": [street_address],
        "postcode": postcode,
        "city": city,
        "same_as_billing": 1
    }
    
    # Add customer info if provided
    if customer_info:
        address.update({
            "firstname": customer_info.firstname,
            "lastname": customer_info.lastname,
            "email": customer_info.email,
            "telephone": customer_info.telephone
        })
        if customer_info.customer_id:
            address["customer_id"] = customer_info.customer_id
    else:
        # Default customer info
        address.update({
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jdoe@example.com",
            "telephone": "(512) 555-1111"
        })
    
    payload = {"address": address}
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/estimate-shipping-methods',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = calculate_shipping_rates(
        city="Purchase", 
        region="New York", 
        postcode="10577", 
        country_id="US", 
        street_address="123 Oak Ave"
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