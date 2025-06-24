import requests
import json
from typing import List, Dict, Any, Optional

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


def retrieve_websites() -> List[Dict[str, Any]]:
    """
    Retrieve a list of all websites from the Magento store.
    
    Returns:
        List[Dict[str, Any]]: A list of website objects, each containing:
            - id (int): The website ID
            - code (str): The website code
            - name (str): The website name
            - default_group_id (int): The default group ID
    
    Example:
        >>> websites = retrieve_websites()
        >>> print(websites)
        [
            {
                "id": 0,
                "code": "admin",
                "name": "Admin",
                "default_group_id": 0
            },
            {
                "id": 1,
                "code": "base",
                "name": "Main Website",
                "default_group_id": 1
            }
        ]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/store/websites"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response.json()

if __name__ == '__main__':
    r = retrieve_websites()
    print(json.dumps(r, indent=4))