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
            'password': 'NewPassword.123'
        })
    )
    return "Bearer " + response.json()


def change_customer_password(currentPassword=None, newPassword=None):
    """
    Change customer password.
    
    Args:
        currentPassword (str): The customer's current password
        newPassword (str): The new password to set
        
    Returns:
        requests.Response: The API response object
        
    Example:
        response = change_customer_password(currentPassword='Password.123', newPassword='NewPassword.123')
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers/me/password"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    assert currentPassword is not None, 'Missing required parameter: currentPassword'
    assert newPassword is not None, 'Missing required parameter: newPassword'
    
    payload = {
        'currentPassword': currentPassword,
        'newPassword': newPassword
    }
    
    response = requests.put(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = change_customer_password(currentPassword='NewPassword.123', newPassword='Password.123')
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