import requests
import json
from urllib.parse import quote

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


def get_guest_cart(cartId):
    """
    Retrieve information for a specified guest cart.
    
    Args:
        cartId (str): The ID of the guest cart to retrieve. Required.
            Example: 'UiqZGvZaXs7zTacs5IJs5hdfpmWAL3Bk' or '277'
    
    Returns:
        Returns detailed information about a specified guest shopping cart including its contents and attributes.
    Raises:
        AssertionError: If cartId is None or not provided.
    
    Example:
        >>> response = get_guest_cart('UiqZGvZaXs7zTacs5IJs5hdfpmWAL3Bk')
        >>> print(response.status_code)
        200
    """
    assert cartId is not None, 'Missing required parameter: cartId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/guest-carts/{quote(str(cartId), safe='')}"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_guest_cart(cartId='UiqZGvZaXs7zTacs5IJs5hdfpmWAL3Bk')
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