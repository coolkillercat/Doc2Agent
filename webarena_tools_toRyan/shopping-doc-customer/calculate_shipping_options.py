import requests, json
from typing import Optional
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
    return "Bearer " + response.text.strip('"')


def calculate_shipping_options(city: str, region: str, postcode: str, country_id: str, street_address: str, customer_details: Optional[dict] = None):
    """
    Calculate shipping costs for available shipping methods.
    
    Args:
        city (str): City name for the shipping address
        region (str): Region or state name for the shipping address
        postcode (str): Postal or ZIP code for the shipping address
        country_id (str): Country ID code (e.g., 'US' for United States)
        street_address (str): Street address for shipping
        customer_details (Optional[dict]): Optional customer details including firstname, lastname, email, telephone
    
    Returns:
        requests.Response: Response object containing available shipping methods and costs
    
    Example:
        response = calculate_shipping_options(
            city="Purchase", 
            region="New York", 
            postcode="10577", 
            country_id="US", 
            street_address="123 Oak Ave",
            customer_details={
                "firstname": "Jane",
                "lastname": "Doe",
                "email": "jdoe@example.com",
                "telephone": "(512) 555-1111"
            }
        )
    """
    # Set up the base URL and endpoint
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = "/rest/default/V1/carts/mine/estimate-shipping-methods"
    
    # Set up headers with authentication token
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token(),
    }
    
    # Prepare the address payload
    address = {
        "region": region,
        "country_id": country_id,
        "street": [street_address],
        "postcode": postcode,
        "city": city,
        "same_as_billing": 1
    }
    
    # Add customer details if provided
    if customer_details:
        address.update({
            "firstname": customer_details.get("firstname", ""),
            "lastname": customer_details.get("lastname", ""),
            "email": customer_details.get("email", ""),
            "telephone": customer_details.get("telephone", "")
        })
    
    # Create the payload
    payload = {
        "address": address
    }
    
    # Make the API request
    response = requests.post(
        url=base_url + endpoint,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = calculate_shipping_options(
        city="Purchase", 
        region="New York", 
        postcode="10577", 
        country_id="US", 
        street_address="123 Oak Ave",
        customer_details={
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jdoe@example.com",
            "telephone": "(512) 555-1111"
        }
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