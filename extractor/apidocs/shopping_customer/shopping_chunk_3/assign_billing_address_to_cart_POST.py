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

def assign_billing_address_to_cart(cartId=None, address=None, useForShipping=None):
    """
    Assign a specified billing address to a specified cart.
    
    Args:
        cartId (str): The cart ID.
        address (dict): The billing address information. The street field should be a list of strings.
        useForShipping (bool): Whether to use the billing address for shipping.
    
    Returns:
        requests.Response: The API response.
    
    Example:
        assign_billing_address_to_cart(
            cartId='cart123',
            address={
                'street': ['123 Main St'],
                'city': 'Anytown',
                'postcode': '12345'
            },
            useForShipping=True
        )
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{cartId}/billing-address"
    
    # Ensure street is a list of strings
    if address and 'street' in address and not isinstance(address['street'], list):
        address['street'] = [address['street']]
    
    payload = {'address': address}
    if useForShipping is not None:
        payload['useForShipping'] = useForShipping
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert cartId is not None, 'Missing required parameter: cartId'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = assign_billing_address_to_cart(cartId='cart123', address={'street': ['123 Main St'], 'city': 'Anytown', 'postcode': '12345'}, useForShipping=True)
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