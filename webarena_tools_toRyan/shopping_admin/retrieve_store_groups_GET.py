import requests
import json
from urllib.parse import quote
import warnings

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


def retrieve_store_groups():
    """
    Retrieves a list of all store groups from the Magento API.
    
    This function makes a GET request to the Magento API endpoint for store groups
    and returns the response object containing the list of store groups.
    
    Returns:
        requests.Response: The response object from the API request.
        
    Example:
        >>> response = retrieve_store_groups()
        >>> store_groups = response.json()
        >>> print(store_groups)
        [
            {
                "id": 0,
                "website_id": 0,
                "root_category_id": 0,
                "default_store_id": 0,
                "name": "Default",
                "code": "default"
            },
            ...
        ]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/store/storeGroups"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = retrieve_store_groups()
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))