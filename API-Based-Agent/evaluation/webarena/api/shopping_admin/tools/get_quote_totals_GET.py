import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_quote_totals():
    """
    Retrieves the totals for the current customer's cart.

    Returns:
        requests.Response: The API response containing cart totals information.

    Note:
        This function requires customer authentication, not admin authentication.
        You need to create a customer token and use that for authorization.
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/carts/mine/totals'

    # For customer cart endpoints, we need a customer token, not admin token
    # This would require a separate customer authentication function
    # For now, we'll use a guest cart approach

    # First, create a guest cart to get a cart ID
    create_cart_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/guest-carts'
    cart_response = requests.post(
        create_cart_url,
        headers={'Content-Type': 'application/json'},
        timeout=50,
        verify=False,
    )

    if cart_response.status_code == 200:
        cart_id = cart_response.json()
        # Now get totals for this guest cart
        guest_totals_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/guest-carts/{cart_id}/totals'
        response = requests.get(
            url=guest_totals_url,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            verify=False,
        )
        return response

    # Fallback to original request if guest cart creation fails
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response


if __name__ == '__main__':
    r = get_quote_totals()
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
