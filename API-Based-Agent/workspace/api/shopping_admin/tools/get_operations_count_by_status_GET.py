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


def get_operations_count_by_status(bulkUuid=None, status=None):
    """
    Get operations count by status for a specific bulk UUID.

    Args:
        bulkUuid (str): The UUID of the bulk operation
        status (int): The status code to filter operations

    Returns:
        Response: The API response object
    """
    assert bulkUuid is not None, 'Missing required parameter: bulkUuid'
    assert status is not None, 'Missing required parameter: status'

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/bulk/{quote(str(bulkUuid), safe='')}/operation-status/{quote(str(status), safe='')}"
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
    r = get_operations_count_by_status(bulkUuid="""abc123""", status=1)
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
