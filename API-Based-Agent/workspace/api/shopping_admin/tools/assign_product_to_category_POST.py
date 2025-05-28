import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def assign_product_to_category(categoryId=None, productSku=None, productLink=None):
    """
    Assign a product to a category.

    Args:
        categoryId (int or str): The ID of the category to assign the product to.
        productSku (str): The SKU of the product to assign.
        productLink (str): The link position of the product in the category.

    Returns:
        requests.Response: The response from the API.
    """
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/categories/{categoryId}/products'
    payload = {
        'productLink': {
            'sku': productSku,
            'position': productLink,
            'category_id': str(categoryId),
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }
    assert categoryId is not None, 'Missing required parameter: categoryId'
    assert productSku is not None, 'Missing required parameter: productSku'
    assert productLink is not None, 'Missing required parameter: productLink'

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = assign_product_to_category(
        categoryId='123', productSku='sample-sku', productLink='0'
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
