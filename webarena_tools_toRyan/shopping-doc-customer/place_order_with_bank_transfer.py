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
    return "Bearer " + response.text.strip('"')


def place_order_with_bank_transfer(email: str, firstname: str, lastname: str, street: list, city: str, region: str, postcode: str, telephone: str, country_id: str = 'US', region_id: int = None, region_code: str = None) -> requests.Response:
    """
    Places an order using bank transfer as the payment method, requiring only essential billing address information and returning the order ID.
    
    Args:
        email (str): Customer's email address
        firstname (str): Customer's first name
        lastname (str): Customer's last name
        street (list): List of street address lines
        city (str): City name
        region (str): Region/state name
        postcode (str): Postal/zip code
        telephone (str): Customer's telephone number
        country_id (str, optional): Country ID code. Defaults to 'US'.
        region_id (int, optional): Region ID. Defaults to None.
        region_code (str, optional): Region code. Defaults to None.
        
    Returns:
        requests.Response: The API response object containing the order ID
        
    Example:
        response = place_order_with_bank_transfer(
            email="jdoe@example.com",
            firstname="Jane",
            lastname="Doe",
            street=["123 Oak Ave"],
            city="Purchase",
            region="New York",
            region_id=43,
            region_code="NY",
            postcode="10577",
            telephone="512-555-1111"
        )
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    payload = {
        "paymentMethod": {
            "method": "banktransfer"
        },
        "billing_address": {
            "email": email,
            "region": region,
            "country_id": country_id,
            "street": street,
            "postcode": postcode,
            "city": city,
            "telephone": telephone,
            "firstname": firstname,
            "lastname": lastname
        }
    }
    
    # Add optional fields if provided
    if region_id is not None:
        payload["billing_address"]["region_id"] = region_id
    
    if region_code is not None:
        payload["billing_address"]["region_code"] = region_code
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = place_order_with_bank_transfer(
        email="jdoe@example.com",
        firstname="Jane",
        lastname="Doe",
        street=["123 Oak Ave"],
        city="Purchase",
        region="New York",
        region_id=43,
        region_code="NY",
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