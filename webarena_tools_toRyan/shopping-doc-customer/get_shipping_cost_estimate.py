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


def get_shipping_cost_estimate(shipping_carrier_code: str = 'tablerate', shipping_method_code: str = 'bestway') -> requests.Response:
    """
    Retrieves the shipping cost estimate for the selected carrier and method by setting shipping and billing information.
    
    Args:
        shipping_carrier_code (str): The shipping carrier code (tablerate or flatrate). Defaults to 'tablerate'.
        shipping_method_code (str): The shipping method code (bestway, tablerate, or flatrate). Defaults to 'bestway'.
        
    Returns:
        requests.Response: The API response containing payment methods and order totals
        
    Example:
        response = get_shipping_cost_estimate('tablerate', 'bestway')
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    payload = {
        "addressInformation": {
            "shipping_address": {
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
            },
            "billing_address": {
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
            },
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = get_shipping_cost_estimate() # no parameter inputs at current stage, need to be filled later.
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