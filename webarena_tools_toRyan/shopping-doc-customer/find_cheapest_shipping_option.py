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
    return response.json()


def find_cheapest_shipping_option(shipping_address: dict):
    """
    Analyzes all available shipping methods for an address and returns the most economical option, helping customers optimize for cost savings.
    
    Args:
        shipping_address (dict): Dictionary containing shipping address details
        
    Returns:
        requests.Response: The API response object
        
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
            "telephone": "(512) 555-1111",
            "same_as_billing": 1
        }
        response = find_cheapest_shipping_option(shipping_address)
    """
    token = get_shopping_customer_auth_token()
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/estimate-shipping-methods"
    
    payload = {
        "address": shipping_address
    }
    
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    # Sample shipping address
    sample_address = {
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
        "telephone": "(512) 555-1111",
        "same_as_billing": 1
    }
    
    r = find_cheapest_shipping_option(sample_address)
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