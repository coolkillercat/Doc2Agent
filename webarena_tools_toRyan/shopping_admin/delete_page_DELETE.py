import requests
import json

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


def delete_page(pageId=None):
    """
    Delete a CMS page by ID.
    
    Args:
        pageId (int): The ID of the page to delete. Required.
        
    Returns:
        dict or bool: Response from the API. True on successful deletion or error message.
        
    Example:
        >>> delete_page(pageId=20)
        True
        
        >>> delete_page(pageId=999)
        {'message': 'The CMS page with the "%1" ID doesn\'t exist.', 'parameters': [999]}
    """
    assert pageId is not None, 'Missing required parameter: pageId'
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770"
    api_url = f"{base_url}/rest/default/V1/cmsPage/{pageId}"
    
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': get_shopping_admin_auth_token()
    }
    
    response = requests.delete(url=api_url, headers=headers, timeout=50, verify=False)
    return response.json()

if __name__ == '__main__':
    r = delete_page(pageId=20)
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = "true"
    result_dict['json'] = r
    result_dict['content'] = "true"
    print(json.dumps(result_dict, indent=4))