import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    """
    Get a customer authentication token from the Magento API.
    
    Returns:
        str: The customer authentication token.
        
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def create_admin_access_token():
    """
    Create an admin access token for the Magento API.
    
    Returns:
        str: The admin authentication token.
        
    Example:
        token = create_admin_access_token()
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token"
    payload = {
        "username": "admin",
        "password": "magento123"
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url=api_url, headers=headers, data=json.dumps(payload), timeout=50)
    return response.json()

if __name__ == '__main__':
    r = create_admin_access_token()
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