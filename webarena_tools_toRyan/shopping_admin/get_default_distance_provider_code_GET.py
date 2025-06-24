import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
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


def get_default_distance_provider_code():
    """
    Get the default distance provider code from the API.
    
    Returns:
        str: The default distance provider code (e.g., 'google')
    
    Example:
        >>> get_default_distance_provider_code()
        'google'
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/inventory/get-distance-provider-code"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response.json()

if __name__ == '__main__':
    r = get_default_distance_provider_code()
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))