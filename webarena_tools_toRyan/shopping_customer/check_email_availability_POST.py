import requests
import json

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


def check_email_availability(customerEmail, websiteId=None):
    """
    Check if given email is associated with a customer account in given website.
    
    Args:
        customerEmail (str): Email address to check availability
        websiteId (int, optional): Website ID to check against. If not set, will use the current websiteId
    
    Returns:
        requests.Response: Response object from the API call
        
    Example:
        response = check_email_availability(customerEmail='example@example.com', websiteId=1)
        is_available = response.json()  # Returns boolean indicating if email is available
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers/isEmailAvailable"
    
    if customerEmail is None:
        raise ValueError('Missing required parameter: customerEmail')
    
    payload = {'customerEmail': customerEmail}
    if websiteId is not None:
        payload['websiteId'] = websiteId
        
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_customer_auth_token()
    }
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    r = check_email_availability(customerEmail='example@example.com', websiteId=1)
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