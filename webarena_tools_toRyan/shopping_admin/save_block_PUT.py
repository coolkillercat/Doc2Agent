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


def save_block(id=None, block_content=None, active=True, identifier=None, title=None, stores=None):
    """
    Save a CMS block using the Magento API.
    
    Args:
        id (str): The ID of the CMS block to update.
        block_content (str): The content of the block (HTML).
        active (bool): Whether the block is active or not.
        identifier (str): The unique identifier for the block.
        title (str): The title of the block.
        stores (list): List of store IDs where the block is available.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        save_block(
            id='2',
            block_content='<p>This is an example block content.</p>',
            active=True,
            identifier='example_block',
            title='Example Block',
            stores=[0, 1]
        )
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    api_url = f"{base_url}/rest/default/V1/cmsBlock/{id}"
    
    assert id is not None, 'Missing required parameter: id'
    
    # Prepare the block data
    block_data = {
        'active': active
    }
    
    if block_content is not None:
        block_data['content'] = block_content
    
    if identifier is not None:
        block_data['identifier'] = identifier
    
    if title is not None:
        block_data['title'] = title
    
    if stores is not None:
        block_data['store_id'] = stores
    
    # Prepare the payload with the required 'block' field
    payload = {
        'block': block_data
    }
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = save_block(id='2', block_content='<p>This is an example block content.</p>', identifier='example_block', title='Example Block')
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