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


def get_product_info(sku=None, editMode=None, storeId=None, forceReload=None):
    """
    Get product information by SKU.

    Args:
        sku (str): The SKU of the product to retrieve.
        editMode (bool, optional): Whether to retrieve the product in edit mode.
        storeId (int, optional): The store ID to retrieve the product from.
        forceReload (bool, optional): Whether to force reload the product.

    Returns:
        requests.Response: The API response containing product information.
    """
    assert sku is not None, 'Missing required parameter: sku'

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/products/{quote(sku, safe='')}"

    # Only include non-None parameters in the query string
    querystring = {}
    if editMode is not None:
        querystring['editMode'] = editMode
    if storeId is not None:
        querystring['storeId'] = storeId
    if forceReload is not None:
        querystring['forceReload'] = forceReload

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(
        url=api_url, headers=headers, params=querystring, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = get_product_info(sku='ABC123', editMode=False, storeId=1, forceReload=False)
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
