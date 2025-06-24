import requests, json
from urllib.parse import quote

def activate_user(user_id: int, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token: str = "GITLAB_KEY_REMOVED"):
    """
    Activates a specified user in the GitLab system. This function can only be used by administrators to reactivate users who have been deactivated.
    
    Args:
        user_id (int): The ID of the user to activate
        base_url (str, optional): The base URL of the GitLab API
        token (str, optional): The private token for authentication
        
    Returns:
        requests.Response: The response from the API call
        
    Example:
        >>> response = activate_user(2330)
        >>> print(response.status_code)
        201
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/users/{user_id}/activate"
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = activate_user(user_id=2330)
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