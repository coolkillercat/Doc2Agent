import requests, json
from urllib.parse import quote


def unban_user(user_id: int) -> requests.Response:
    """
    Unbans a previously banned user from the GitLab platform. Only available for administrators.
    
    This endpoint requires administrator privileges to use.
    
    Parameters:
        user_id (int): The ID of the user to unban
        
    Returns:
        requests.Response: The API response object
        
    Example:
        >>> response = unban_user(2330)
        >>> response.status_code
        201
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    url = f"{base_url}/users/{user_id}/unban"
    return requests.post(url, headers=headers)


if __name__ == '__main__':
    r = unban_user(user_id=2330)
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