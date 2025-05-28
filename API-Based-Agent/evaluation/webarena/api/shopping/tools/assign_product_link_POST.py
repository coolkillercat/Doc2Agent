import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def assign_product_link(sku=None):
    """
    Assigns product links to a specified product by SKU.

    Args:
        sku (str): The SKU of the product to assign links to.

    Returns:
        requests.Response: The API response object.
    """
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/products/{sku}/links'

    # The error indicates that 'items' field is required
    payload = {
        'items': [
            {
                'sku': sku,
                'link_type': 'related',  # Assuming a default link type
                'linked_product_sku': 'sample_linked_sku',  # Sample linked product
                'position': 1,  # Default position
            }
        ]
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
    r = assign_product_link(sku="""ABC123""")
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
