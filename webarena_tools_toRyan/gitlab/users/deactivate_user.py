import requests, json
from urllib.parse import quote


def deactivate_user(user_id: int, base_url=None, token=None):
    """
    Deactivates a specified user in the GitLab system. This function can only be used by administrators 
    and is useful for managing user access when accounts become dormant.
    
    Args:
        user_id (int): The ID of the user to be deactivated.
        base_url (str, optional): The base URL for the GitLab API. Defaults to the configured URL.
        token (str, optional): The private token for authentication. Defaults to the configured token.
        
    Returns:
        requests.Response: The response from the API call.
        
    Example:
        >>> response = deactivate_user(2330)
        >>> print(response.status_code)
        201
    """
    if base_url is None:
        base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    if token is None:
        token = 'GITLAB_KEY_REMOVED'
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/users/{user_id}/deactivate"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = deactivate_user(user_id=2330)
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