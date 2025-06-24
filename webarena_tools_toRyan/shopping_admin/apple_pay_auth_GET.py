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


def apple_pay_auth():
    """
    Returns details required to be able to submit a payment with Apple Pay.
    
    This function makes a GET request to the Apple Pay authentication endpoint
    and returns the response containing client token and other payment details.
    
    Returns:
        requests.Response: The response object from the API call
        
    Example:
        >>> response = apple_pay_auth()
        >>> print(response.status_code)
        200
        >>> print(response.json())
        {
            "client_token": "",
            "display_name": "Store",
            "action_success": "http://example.com/checkout/onepage/success/",
            "logged_in": false,
            "store_code": "default"
        }
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/applepay/auth"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = apple_pay_auth()
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