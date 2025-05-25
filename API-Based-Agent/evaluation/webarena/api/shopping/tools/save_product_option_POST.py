import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def save_product_option(sku=None):
    """
    Save a configurable product option for a specific SKU.

    Args:
        sku (str): The SKU of the product to save options for.

    Returns:
        requests.Response: The API response object.
    """
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/configurable-products/{sku}/options'

    # The API requires an 'option' field
    payload = {
        'option': {
            'attribute_id': 'color',  # Example attribute ID
            'label': 'Color',  # Example label
            'position': 0,  # Example position
            'values': [
                {
                    'value_index': 1  # Example value index
                }
            ],
        }
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
    r = save_product_option(sku="""ABC123""")
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
