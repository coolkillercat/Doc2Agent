import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
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

def create_customer_account(customer=None, password=None, redirectUrl=None):
    """
    Create customer account. Perform necessary business operations like sending email.
    
    Args:
        customer (dict): Customer information including email, firstname, and lastname.
            Example: {'email': 'example@example.com', 'firstname': 'John', 'lastname': 'Doe'}
        password (str): Customer password. Must contain at least 3 of the following character classes:
            lowercase letters, uppercase letters, digits, and special characters.
            Example: 'Password123!'
        redirectUrl (str, optional): URL to redirect after account creation.
            Example: 'http://example.com/welcome'
    
    Returns:
        requests.Response: The API response object
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers"
    payload = {'customer': customer, 'password': password}
    if redirectUrl:
        payload['redirectUrl'] = redirectUrl
    
    headers = {
        "Content-Type": "application/json"
    }
    
    assert customer is not None, 'Missing required parameter: customer'
    assert password is not None, 'Missing required parameter: password'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_customer_account(
        customer={'email': 'example@example.com', 'firstname': 'John', 'lastname': 'Doe'}, 
        password='Password123!', 
        redirectUrl='http://example.com/welcome'
    )
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