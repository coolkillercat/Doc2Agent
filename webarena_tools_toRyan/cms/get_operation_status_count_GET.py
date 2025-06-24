import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    """
    Get authentication token for shopping admin API.
    
    Returns:
        str: Bearer token for API authentication
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return "Bearer " + response.json()


def get_operation_status_count(bulkUuid=None, status=None):
    """
    Get operations count by bulk uuid and status.
    
    Args:
        bulkUuid (str): The bulk UUID identifier
        status (int): The status code to filter operations
    
    Returns:
        Returns the count of operations with a specific status for a given bulk UUID.
    Example:
        >>> get_operation_status_count(bulkUuid='abc123-uuid', status=1)
    """
    assert bulkUuid is not None, 'Missing required parameter: bulkUuid'
    assert status is not None, 'Missing required parameter: status'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780"
    api_url = f"{base_url}/rest/default/V1/bulk/{quote(str(bulkUuid), safe='')}/operation-status/{status}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_operation_status_count(bulkUuid='abc123-uuid', status=1)
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
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))