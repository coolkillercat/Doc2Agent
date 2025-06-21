import requests
import json

def get_shopping_customer_auth_token():
    """
    get_shopping_customer_auth_token function.
    
    Returns:
        Returns an array of available shipping methods with their carrier codes, titles, costs, and tax information for the customer's cart.
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

def estimate_shipping_costs(address):
    """
    Estimates shipping costs for the customer's cart based on the provided shipping address.
    
    Args:
        address (dict): Customer's shipping address information
        
    Returns:
        list: Available shipping methods and their costs
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/estimate-shipping-methods'
    
    payload = {"address": address}
    
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    # Example usage
    address = {
        "region": "New York",
        "region_id": 43,
        "region_code": "NY",
        "country_id": "US",
        "street": ["123 Oak Ave"],
        "postcode": "10577",
        "city": "Purchase",
        "firstname": "Jane",
        "lastname": "Doe",
        "customer_id": 4,
        "email": "jdoe@example.com",
        "telephone": "(512) 555-1111",
        "same_as_billing": 1
    }
    
    r = estimate_shipping_costs(address)
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))