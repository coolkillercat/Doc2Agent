import json
from urllib.parse import quote

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_bundle_product_children(productSku=None, optionId=None):
    """
    Get children of bundle product

    Args:
        productSku (str): SKU of the bundle product
        optionId (int, optional): Option ID to filter results

    Returns:
        requests.Response: API response object
    """
    assert productSku is not None, 'Missing required parameter: productSku'

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/bundle-products/{quote(productSku, safe='')}/children"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    params = {}
    if optionId is not None:
        params['optionId'] = optionId

    response = requests.get(
        url=api_url, headers=headers, params=params, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = get_bundle_product_children(productSku='sku123', optionId=1)
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
