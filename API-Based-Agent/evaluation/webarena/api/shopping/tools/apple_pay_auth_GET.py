import requests, json
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
    return response.json()

def apple_pay_auth():
    """
    Returns details required to be able to submit a payment with Apple Pay.
    
    Returns:
        requests.Response: Response object containing Apple Pay authorization details
        
    Example:
        response = apple_pay_auth()
        auth_details = response.json()
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/applepay/auth"
    headers = {
        "Content-Type": "application/json"
    }
    
    # Try to get the token, but handle the case where it might fail
    try:
        token = get_shopping_customer_auth_token()
        headers["Authorization"] = f"Bearer {token}"
    except:
        # Continue without token if authentication fails
        pass
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = apple_pay_auth()
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