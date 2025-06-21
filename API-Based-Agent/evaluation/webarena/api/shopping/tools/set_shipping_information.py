import requests
import json

def get_shopping_customer_auth_token():
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

def set_shipping_information(shipping_address: dict, billing_address: dict, shipping_carrier_code: str, shipping_method_code: str) -> dict:
    """
    Sets shipping and billing information for the cart, returning available payment methods and order totals.
    
    Args:
        shipping_address (dict): The shipping address information including region, region_id, region_code, 
                                country_id, street, postcode, city, firstname, lastname, email, telephone
        billing_address (dict): The billing address information including the same fields as shipping_address
        shipping_carrier_code (str): The shipping carrier code (e.g., 'flatrate', 'tablerate')
        shipping_method_code (str): The shipping method code (e.g., 'flatrate', 'bestway')
        
    Returns:
        dict: Response containing payment methods and order totals
        
    Example:
        shipping_address = {
            "region": "New York",
            "region_id": 43,
            "region_code": "NY",
            "country_id": "US",
            "street": ["123 Oak Ave"],
            "postcode": "10577",
            "city": "Purchase",
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jdoe@example.com",
            "telephone": "512-555-1111"
        }
        
        billing_address = {
            "region": "New York",
            "region_id": 43,
            "region_code": "NY",
            "country_id": "US",
            "street": ["123 Oak Ave"],
            "postcode": "10577",
            "city": "Purchase",
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "jdoe@example.com",
            "telephone": "512-555-1111"
        }
        
        result = set_shipping_information(
            shipping_address=shipping_address,
            billing_address=billing_address,
            shipping_carrier_code="flatrate",
            shipping_method_code="flatrate"
        )
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = "/rest/default/V1/carts/mine/shipping-information"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {get_shopping_customer_auth_token()}'
    }
    
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    response = requests.post(
        url=base_url + endpoint,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response.json()

if __name__ == '__main__':
    # Sample shipping and billing address
    shipping_address = {
        "region": "New York",
        "region_id": 43,
        "region_code": "NY",
        "country_id": "US",
        "street": ["123 Oak Ave"],
        "postcode": "10577",
        "city": "Purchase",
        "firstname": "Jane",
        "lastname": "Doe",
        "email": "jdoe@example.com",
        "telephone": "512-555-1111"
    }
    
    billing_address = {
        "region": "New York",
        "region_id": 43,
        "region_code": "NY",
        "country_id": "US",
        "street": ["123 Oak Ave"],
        "postcode": "10577",
        "city": "Purchase",
        "firstname": "Jane",
        "lastname": "Doe",
        "email": "jdoe@example.com",
        "telephone": "512-555-1111"
    }
    
    # Set shipping carrier and method
    shipping_carrier_code = "flatrate"
    shipping_method_code = "flatrate"
    
    r = set_shipping_information(
        shipping_address=shipping_address,
        billing_address=billing_address,
        shipping_carrier_code=shipping_carrier_code,
        shipping_method_code=shipping_method_code
    )
    
    r_json = r
    
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))