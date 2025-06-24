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


def save_block(block_data):
    """
    Save a CMS block using the Magento API.
    
    Args:
        block_data (dict): A dictionary containing the block data to be saved.
            Must include a 'block' key with block details.
            
    Example:
        block_data = {
            "block": {
                "identifier": "example_block",
                "title": "Example Block",
                "content": "<p>This is an example block content.</p>",
                "active": True
            }
        }
        response = save_block(block_data)
        
    Returns:
        requests.Response: The API response object
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/cmsBlock"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    assert block_data is not None, 'Missing required parameter: block_data'
    assert 'block' in block_data, 'Missing required field: block'
    
    response = requests.post(url=api_url, json=block_data, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example block data with required 'block' field
    example_block_data = {
        "block": {
            "identifier": "example_block",
            "title": "Example Block",
            "content": "<p>This is an example block content.</p>",
            "active": True
        }
    }
    
    r = save_block(example_block_data)
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