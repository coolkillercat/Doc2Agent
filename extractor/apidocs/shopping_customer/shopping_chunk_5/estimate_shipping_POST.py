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

def estimate_shipping(cartId=None):
    """
    Estimate shipping methods for a guest gift registry.
    
    Args:
        cartId (str): The ID of the cart for which to estimate shipping methods.
            Example: '12345', 'cart123', 'guest123'
    
    Returns:
        requests.Response: The API response object containing shipping method estimates.
    
    Raises:
        AssertionError: If cartId is not provided.
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{cartId}/estimate-shipping-methods"
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url=api_url, headers=headers, timeout=50, verify=False, data=json.dumps({}))
    return response

if __name__ == '__main__':
    r = estimate_shipping(cartId='12345')
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