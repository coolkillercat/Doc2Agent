import json
from urllib.parse import quote

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_product_links(sku=None, type=None):
    """
    Get product links for a specific SKU and link type.

    Args:
        sku (str): The SKU of the product
        type (str): The type of link (related, upsell, crosssell, etc.)

    Returns:
        Response object from the API request
    """
    assert sku is not None, 'Missing required parameter: sku'
    assert type is not None, 'Missing required parameter: type'

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/products/{quote(sku, safe='')}/links/{quote(type, safe='')}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
        response = response2
    return response


if __name__ == '__main__':
    r = get_product_links(sku='ABC123', type='related')
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
