import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def add_child_product_to_bundle_option(sku=None, optionId=None, linkedProduct=None):
    """
    Add a child product to a bundle option.

    Args:
        sku (str): The SKU of the bundle product.
        optionId (int): The ID of the bundle option.
        linkedProduct (str): The SKU of the product to link to the bundle option.

    Returns:
        Response: The API response.
    """
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/bundle-products/{sku}/links/{optionId}'
    payload = {'linkedProduct': linkedProduct}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }
    assert sku is not None, 'Missing required parameter: sku'
    assert optionId is not None, 'Missing required parameter: optionId'
    assert linkedProduct is not None, 'Missing required parameter: linkedProduct'

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = add_child_product_to_bundle_option(
        sku='sku123', optionId=1, linkedProduct='linked_product_sku'
    )
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
