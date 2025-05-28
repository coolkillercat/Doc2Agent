import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def get_currency_information():
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/directory/currency'
    querystring = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.get(
        url=api_url, headers=headers, params=querystring, timeout=50, verify=False
    )
    if response.status_code != 200:
        response2 = requests.get(
            url=api_url, timeout=50
        )  # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())


if __name__ == '__main__':
    r = get_currency_information()
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
