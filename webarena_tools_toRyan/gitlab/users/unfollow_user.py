import requests, json
from urllib.parse import quote



def unfollow_user(user_id: int) -> dict:
    """
    Unfollow a specified GitLab user by their user ID. Returns the details of the user that was unfollowed.
    
    Args:
        user_id (int): The ID of the user to unfollow.
        
    Returns:
        Returns details of the GitLab user that was unfollowed after sending an unfollow request to the specified user ID."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"/users/{user_id}/unfollow"
    url = f"{base_url}{endpoint}"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = unfollow_user(user_id=2330)
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