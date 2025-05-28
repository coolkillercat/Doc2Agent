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


def get_stock_status_by_sku(productSku=None, scopeId=None):
    """
    Get stock status information for a specific product by SKU.

    Args:
        productSku (str): The SKU of the product to retrieve stock status for
        scopeId (int, optional): The scope ID for the request

    Returns:
        requests.Response: The API response containing stock status information

    Raises:
        AssertionError: If productSku is not provided
    """
    assert productSku is not None, 'Missing required parameter: productSku'

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/stockStatuses/{quote(productSku, safe='')}"

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
    r = get_stock_status_by_sku(productSku='SKU12345', scopeId=1)
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
