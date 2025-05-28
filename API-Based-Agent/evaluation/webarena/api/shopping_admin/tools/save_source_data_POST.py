import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def save_source_data():
    """
    Save inventory source data to the API.

    Returns:
        Response object from the API request
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/inventory/sources'
    payload = {
        'source': {
            'name': 'Default Source',
            'source_code': 'default',
            'enabled': True,
            'description': 'Default inventory source',
            'country_id': 'US',
            'postcode': '10001',
            'use_default_carrier_config': True,
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = save_source_data()
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
