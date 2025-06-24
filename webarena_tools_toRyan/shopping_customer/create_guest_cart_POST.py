import requests
import json
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
    return "Bearer " + response.json()


def create_guest_cart():
    """
    Create an empty cart and quote for an anonymous customer.
    
    This function makes a POST request to the guest-carts endpoint to create
    a new empty cart for an anonymous customer. No authentication token is needed
    for guest cart creation.
    
    Returns:
        requests.Response: The API response containing the cart ID
        
    Example:
        response = create_guest_cart()
        cart_id = response.json()
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = create_guest_cart()
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