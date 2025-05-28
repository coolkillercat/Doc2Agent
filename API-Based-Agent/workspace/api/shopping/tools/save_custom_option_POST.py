import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def save_custom_option():
    """
    Save a custom product option to the Magento API.

    Returns:
        requests.Response: The API response object
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/products/options'
    payload = {
        'option': {
            'product_sku': 'sample-sku',
            'title': 'Custom Option',
            'type': 'field',
            'is_require': True,
            'sort_order': 1,
            'price': 0,
            'price_type': 'fixed',
            'max_characters': 100,
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = save_custom_option()
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
