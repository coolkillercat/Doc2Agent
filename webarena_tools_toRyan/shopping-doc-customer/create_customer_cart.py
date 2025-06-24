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
    return "Bearer " + response.json().strip('"')


def create_customer_cart() -> requests.Response:
    """
    Creates a new shopping cart for the authenticated customer and returns the quote ID (cart ID) 
    which is required for subsequent cart operations.
    
    Returns:
        requests.Response: The API response containing the quoteId
        
    Example:
        response = create_customer_cart()
        quote_id = response.json()
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine'
    
    response = requests.post(url=url, headers=headers)
    return response

if __name__ == '__main__':
    r = create_customer_cart() # no parameter inputs at current stage, need to be filled later.
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