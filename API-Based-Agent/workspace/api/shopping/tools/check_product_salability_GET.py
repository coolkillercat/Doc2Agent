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


def check_product_salability(sku=None, stockId=None):
    """
    Check if a product is salable for a given stock ID.

    Args:
        sku (str): The SKU of the product to check
        stockId (int): The stock ID to check against

    Returns:
        requests.Response: The API response
    """
    assert sku is not None, 'Missing required parameter: sku'
    assert stockId is not None, 'Missing required parameter: stockId'

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/is-product-salable/{quote(str(sku), safe='')}/{quote(str(stockId), safe='')}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(
            url=api_url, timeout=50
        )  # in case API can't handle redundant params
        response = response2
    return response


if __name__ == '__main__':
    r = check_product_salability(sku="""ABC123""", stockId=1)
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
