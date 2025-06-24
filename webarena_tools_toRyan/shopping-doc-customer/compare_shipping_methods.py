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
    return response.text.strip('"')


def compare_shipping_methods(postal_code: str, country_code: str, region_code: str = None, city: str = None, 
                            street: list = None, firstname: str = None, lastname: str = None, 
                            email: str = None, telephone: str = None):
    """
    Estimates shipping costs for available shipping methods based on address information.
    
    Args:
        postal_code (str): The postal/zip code for shipping (e.g., '10577')
        country_code (str): The country code (e.g., 'US')
        region_code (str, optional): The region/state code (e.g., 'NY')
        city (str, optional): The city name (e.g., 'Purchase')
        street (list, optional): List of street address lines (e.g., ['123 Oak Ave'])
        firstname (str, optional): First name for shipping
        lastname (str, optional): Last name for shipping
        email (str, optional): Email address
        telephone (str, optional): Phone number
        
    Returns:
        requests.Response: Response from the shipping estimation API
        
    Example:
        response = compare_shipping_methods('10577', 'US', 'NY', 'Purchase')
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = "/rest/default/V1/carts/mine/estimate-shipping-methods"
    
    # Get the auth token
    auth_token = get_shopping_customer_auth_token()
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {auth_token}'
    }
    
    # Build the address payload
    address = {
        "country_id": country_code,
        "postcode": postal_code
    }
    
    # Add optional parameters if provided
    if region_code:
        address["region_code"] = region_code
    
    if city:
        address["city"] = city
        
    if street:
        address["street"] = street
        
    if firstname:
        address["firstname"] = firstname
        
    if lastname:
        address["lastname"] = lastname
        
    if email:
        address["email"] = email
        
    if telephone:
        address["telephone"] = telephone
    
    # Create the full payload
    payload = {
        "address": address
    }
    
    # Make the API request
    response = requests.post(
        url=f"{base_url}{endpoint}",
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = compare_shipping_methods('10577', 'US', 'NY', 'Purchase')
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