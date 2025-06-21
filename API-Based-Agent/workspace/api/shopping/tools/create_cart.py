import requests, json
from urllib.parse import quote

import json
import requests

def get_shopping_customer_auth_token():
    """
    get_shopping_customer_auth_token function.
    
    Returns:
        Returns the quote ID (cart ID) that is used for subsequent cart-related API operations.
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


def create_cart():
    """
    Creates a new shopping cart for the customer and returns the quoteId (cart ID).
    
    Returns:
        Response object containing the quoteId for the newly created cart.
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    endpoint = "/rest/default/V1/carts/mine"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_shopping_customer_auth_token()
    }
    
    response = requests.post(
        url=f"{base_url}{endpoint}",
        headers=headers
    )
    
    return response

if __name__ == '__main__':
    r = create_cart()
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