import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def update_downloadable_link(sku=None):
    """
    Update downloadable link for a product.

    Args:
        sku (str): The SKU of the product to update.

    Returns:
        requests.Response: The API response.
    """
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/products/{sku}/downloadable-links'
    payload = {
        'isGlobalScopeContent': True,
        'link': {
            'title': 'Downloadable Product',
            'sort_order': 0,
            'is_shareable': 1,
            'price': 0,
            'number_of_downloads': 0,
            'link_type': 'file',
            'link_file': '/sample/sample.pdf',
            'sample_type': 'file',
            'sample_file': '/sample/sample.pdf',
        },
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }
    assert sku is not None, 'Missing required parameter: sku'

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = update_downloadable_link(sku="""ABC123""")
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
