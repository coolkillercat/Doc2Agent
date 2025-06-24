import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return "Bearer " + response.json()


def create_guest_cart():
    """
    Creates an empty cart and quote for a guest.
    
    Returns:
        int: The cart ID for the newly created guest cart.
        
    Example:
        >>> cart_id = create_guest_cart()
        >>> print(cart_id)
        268
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/carts/"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, headers=headers, timeout=50, verify=False)
    return response.json()

if __name__ == '__main__':
    r = create_guest_cart()
    r_json = None
    try:
        r_json = r
    except:
        pass
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(str(r))
    result_dict['json'] = r
    result_dict['content'] = json.dumps(str(r))
    print(json.dumps(result_dict, indent=4))