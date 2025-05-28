import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_cart_information():
    """
    Retrieves the shopping cart information for the current customer.

    Returns:
        requests.Response: The API response containing cart information.
    """
    # Admin token cannot be used for customer cart operations
    # Need to create a customer token or use a different approach

    # First, create a guest cart
    create_cart_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts'
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        url=create_cart_url, headers=headers, timeout=50, verify=False
    )

    if response.status_code == 200:
        cart_id = response.json()
        # Now get the guest cart information
        api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/guest-carts/{cart_id}'
        response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)

    return response


if __name__ == '__main__':
    r = get_cart_information()
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
