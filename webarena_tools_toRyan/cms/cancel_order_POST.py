import requests
import json

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


def cancel_order(id):
    """
    Cancels a specified order.
    
    Args:
        id (int): The order ID to cancel. This parameter is required.
        
    Returns:
        Returns a boolean value indicating whether the specified order was successfully canceled.
    Example:
        >>> response = cancel_order(id=40)
        >>> print(response.status_code)
        200
        >>> print(response.json())
        True
    """
    if id is None:
        raise ValueError('Missing required parameter: id')
    
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    api_url = f"{base_url}/rest/default/V1/orders/{id}/cancel"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.post(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = cancel_order(id=40)
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