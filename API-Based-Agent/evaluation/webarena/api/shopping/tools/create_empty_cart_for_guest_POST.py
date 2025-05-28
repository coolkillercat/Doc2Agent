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

def create_empty_cart_for_guest():
    """
    Creates an empty cart and quote for an anonymous customer.
    
    This function sends a POST request to the guest-carts endpoint to create
    a new empty cart for a guest user. No authentication token is required.
    
    Returns:
        requests.Response: The response object from the API request.
        
    Example:
        >>> create_empty_cart_for_guest()
        <Response [200]>
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts"
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_empty_cart_for_guest()
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