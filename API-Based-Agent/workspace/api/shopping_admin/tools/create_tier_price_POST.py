import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def create_tier_price(sku=None, customerGroupId=None, qty=None, price=None):
    api_url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price}'
    payload = {
        'sku': sku,
        'customerGroupId': customerGroupId,
        'qty': qty,
        'price': price,
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }
    assert sku is not None, 'Missing required parameter: sku'
    assert customerGroupId is not None, 'Missing required parameter: customerGroupId'
    assert qty is not None, 'Missing required parameter: qty'
    assert price is not None, 'Missing required parameter: price'

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response
    # print(response.json())


if __name__ == '__main__':
    r = create_tier_price(
        sku="""ABC123""", customerGroupId="""all""", qty=10, price=99.99
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
