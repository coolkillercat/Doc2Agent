import requests, json
from urllib.parse import quote

def ban_user(user_id: int) -> dict:
    """
    Bans a specified user from the GitLab instance. This function is available only for administrators and helps maintain platform security by preventing problematic users from accessing the system.
    
    Args:
        user_id (int): The ID of the user to ban.
        
    Returns:
        dict: The API response object
        
    Example:
        >>> response = ban_user(user_id=2330)
        >>> response.status_code
        201
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/users/{user_id}/ban"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = ban_user(user_id=2330)
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