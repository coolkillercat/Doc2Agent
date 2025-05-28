import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def assign_billing_address(cartId=None):
    """
    Assigns a billing address to a cart.

    Args:
        cartId: The ID of the cart to assign the billing address to.

    Returns:
        The API response object.
    """
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/{cartId}/billing-address'

    # Include address in the payload as it's required according to the error
    payload = {
        'address': {
            'firstname': 'John',
            'lastname': 'Doe',
            'street': ['123 Main St'],
            'city': 'Anytown',
            'region_code': 'NY',
            'region': 'New York',
            'postcode': '10001',
            'country_id': 'US',
            'telephone': '1234567890',
            'email': 'john.doe@example.com',
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
    r = assign_billing_address(cartId=123)
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
