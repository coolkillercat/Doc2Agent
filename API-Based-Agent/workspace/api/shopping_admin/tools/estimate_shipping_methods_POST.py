import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def estimate_shipping_methods(cartId=None):
    """
    Estimate shipping methods for a cart by providing cart ID and address information.

    Args:
        cartId: The ID of the cart to estimate shipping methods for

    Returns:
        Response object from the API call
    """
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/{cartId}/estimate-shipping-methods'
    payload = {
        'address': {
            'region': 'New York',
            'regionId': 43,
            'regionCode': 'NY',
            'countryId': 'US',
            'street': ['123 Main St'],
            'postcode': '10001',
            'city': 'New York',
            'firstname': 'John',
            'lastname': 'Doe',
            'telephone': '1234567890',
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }
    assert cartId is not None, 'Missing required parameter: cartId'

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = estimate_shipping_methods(cartId="""123""")
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
    result_dict['content'] = r.content.decode('utf-8')
    print(json.dumps(result_dict, indent=4))
