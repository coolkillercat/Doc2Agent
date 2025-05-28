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


def retrieve_cms_block(blockId=None):
    """
    Retrieve CMS block information by blockId.

    Args:
        blockId: The ID of the CMS block to retrieve

    Returns:
        Response object from the API request
    """
    assert blockId is not None, 'Missing required parameter: blockId'

    # Handle tuple input if provided
    if isinstance(blockId, tuple):
        blockId = blockId[1]

    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/cmsBlock/{quote(str(blockId), safe='')}"

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
    r = retrieve_cms_block(blockId=('combined_shopping', 'block123'))
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
