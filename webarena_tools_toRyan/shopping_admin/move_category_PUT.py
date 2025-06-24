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


def move_category(categoryId=None, parentId=None, afterId=None):
    """
    Move a category to a new parent category.
    
    Args:
        categoryId (int): The ID of the category to move (required)
        parentId (int): The ID of the new parent category (required)
        afterId (int, optional): The ID of the category after which to place the moved category
    
    Returns:
        requests.Response: The API response object
    
    Examples:
        >>> move_category(categoryId=11, parentId=2)
        >>> move_category(categoryId=11, parentId=2, afterId=3)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/categories/{categoryId}/move"
    
    assert categoryId is not None, 'Missing required parameter: categoryId'
    assert parentId is not None, 'Missing required parameter: parentId'
    
    payload = {'parentId': parentId}
    if afterId is not None:
        payload['afterId'] = afterId
    
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    response = requests.put(url=api_url, json=payload, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = move_category(categoryId=11, parentId=2, afterId=3)
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