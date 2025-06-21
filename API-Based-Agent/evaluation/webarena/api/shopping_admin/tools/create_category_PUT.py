import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
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


def create_category(id=None, name=None, parent_id=None, is_active=True, include_in_menu=True, position=0, available_sort_by=None, custom_attributes=None):
    """
    Create or update a category in the shopping system.
    
    Args:
        id (str): The ID of the category to create or update.
        name (str): The name of the category.
        parent_id (int): The ID of the parent category.
        is_active (bool): Whether the category is active.
        include_in_menu (bool): Whether to include the category in the menu.
        position (int): The position of the category.
        available_sort_by (list): List of available sort options.
        custom_attributes (list): List of custom attributes.
        
    Returns:
        Returns category details including ID, name, hierarchy information, status, and any custom attributes after creating or updating a category in the shopping system.
    Example:
        >>> create_category(id='11', name='Electronics', parent_id=2, is_active=True, include_in_menu=True, position=9)
    """
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    api_url = f"{base_url}/rest/default/V1/categories/{id}"
    
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    
    payload = {
        'category': {
            'id': id,
            'name': name,
            'is_active': is_active,
            'include_in_menu': include_in_menu,
            'position': position
        }
    }
    
    if parent_id is not None:
        payload['category']['parent_id'] = parent_id
    
    if available_sort_by is not None:
        payload['category']['available_sort_by'] = available_sort_by
        
    if custom_attributes is not None:
        payload['category']['custom_attributes'] = custom_attributes
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_category(id='11', name='Electronics', parent_id=2)
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