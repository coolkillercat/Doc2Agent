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


def get_source_selection_algorithm_list():
    """
    Retrieves the list of available source selection algorithms from the inventory API.
    
    This function makes a GET request to the inventory source selection algorithm list endpoint
    and returns the response object containing the available algorithms.
    
    Returns:
        requests.Response: The response object from the API request.
        
    Example:
        >>> response = get_source_selection_algorithm_list()
        >>> algorithms = response.json()
        >>> print(algorithms)
        [
            {
                "code": "distance",
                "title": "Distance Priority",
                "description": "Algorithm which provides Source Selections based on shipping address distance from the source"
            },
            {
                "code": "priority",
                "title": "Source Priority",
                "description": "Algorithm which provides Source Selections based on predefined priority of Source"
            }
        ]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/inventory/source-selection-algorithm-list"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_source_selection_algorithm_list()
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