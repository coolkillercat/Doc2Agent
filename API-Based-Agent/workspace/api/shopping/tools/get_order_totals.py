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


def get_order_totals(
    shipping_address=None, 
    billing_address=None, 
    shipping_carrier_code="flatrate", 
    shipping_method_code="flatrate"
) -> dict:
    """
    Retrieves the detailed breakdown of the current order's totals, including subtotal, shipping, taxes, and grand total.
    
    This function sets the shipping and billing information for the cart, which returns available payment methods
    and calculates order totals.
    
    Args:
        shipping_address (dict, optional): Shipping address information. Defaults to a sample address.
        billing_address (dict, optional): Billing address information. Defaults to the same as shipping address.
        shipping_carrier_code (str, optional): Carrier code. Defaults to "flatrate".
        shipping_method_code (str, optional): Method code. Defaults to "flatrate".
    
    Returns:
        dict: The API response containing payment methods and order totals
        
    Example:
        totals = get_order_totals()
        
        # With custom shipping address
        custom_address = {
            "region": "California",
            "region_id": 12,
            "region_code": "CA",
            "country_id": "US",
            "street": ["456 Palm St"],
            "postcode": "90210",
            "city": "Beverly Hills",
            "firstname": "John",
            "lastname": "Smith",
            "email": "jsmith@example.com",
            "telephone": "213-555-1212"
        }
        totals = get_order_totals(shipping_address=custom_address)
    """
    token = get_shopping_customer_auth_token()
    headers = {'Content-Type': 'application/json', 'Authorization': token}
    
    # Default shipping address if none provided
    default_address = {
        "region": "New York",
        "region_id": 43,
        "region_code": "NY",
        "country_id": "US",
        "street": [
            "123 Oak Ave"
        ],
        "postcode": "10577",
        "city": "Purchase",
        "firstname": "Jane",
        "lastname": "Doe",
        "email": "jdoe@example.com",
        "telephone": "512-555-1111"
    }
    
    if shipping_address is None:
        shipping_address = default_address
    
    if billing_address is None:
        billing_address = shipping_address
    
    payload = {
        "addressInformation": {
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "shipping_carrier_code": shipping_carrier_code,
            "shipping_method_code": shipping_method_code
        }
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response.json()

if __name__ == '__main__':
    r = get_order_totals() # no parameter inputs at current stage, need to be filled later.
    r_json = None
    try:
        r_json = r
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))