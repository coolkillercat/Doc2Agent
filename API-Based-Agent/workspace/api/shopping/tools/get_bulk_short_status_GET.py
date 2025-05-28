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


def get_bulk_short_status(bulkUuid=None):
    """
    Get the status of a bulk operation by its UUID.

    Args:
        bulkUuid: The UUID of the bulk operation to check

    Returns:
        Response object from the API request
    """
    assert bulkUuid is not None, 'Missing required parameter: bulkUuid'

    # Extract the actual UUID if it's in a tuple format
    if isinstance(bulkUuid, tuple) or isinstance(bulkUuid, set):
        bulkUuid = bulkUuid[1] if isinstance(bulkUuid, tuple) else list(bulkUuid)[1]

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/bulk/{quote(str(bulkUuid), safe='')}/status"

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
    r = get_bulk_short_status(bulkUuid=('combined_shopping', 'abc123'))
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
