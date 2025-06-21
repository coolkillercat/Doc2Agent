import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
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


def create_customer_cart(customerId):
    """
    Creates an empty cart and quote for a specified customer if customer does not have a cart yet.
    
    Args:
        customerId (int): The customer ID.
        
    Returns:
        Returns a cart ID for a specified customer after creating an empty cart and quote.
    Example:
        >>> create_customer_cart(customerId=1)
        >>> create_customer_cart(customerId=4)
    """
    assert customerId is not None, 'Missing required parameter: customerId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/customers/{customerId}/carts"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.post(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_customer_cart(customerId=1)
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