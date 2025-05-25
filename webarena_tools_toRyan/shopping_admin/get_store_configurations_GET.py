import requests, json
from urllib.parse import quote

def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url=f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={
            'content-type': 'application/json'
        },
        data=json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return response.json()

def get_store_configurations(storeCodes=None):
    """
    Get store configurations from the Magento API.
    
    Args:
        storeCodes (list, optional): List of store codes to retrieve configurations for.
        
    Returns:
        requests.Response: The API response object.
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/store/storeConfigs"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_admin_admin_auth_token(),
    }
    
    params = {}
    if storeCodes:
        params['storeCodes'] = ','.join(storeCodes) if isinstance(storeCodes, list) else storeCodes
    
    response = requests.get(url=api_url, headers=headers, params=params, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_store_configurations()
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