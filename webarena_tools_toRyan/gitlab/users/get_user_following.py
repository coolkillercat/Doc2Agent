import requests, json
from urllib.parse import quote



def get_user_following(user_id: int) -> list:
    """
    Retrieve a list of users who the specified GitLab user is following. Returns details of followed users including ID, name, username, and profile information.
    
    Args:
        user_id (int): The ID of the user whose following list is to be retrieved
        
    Returns:
        Returns a list of users that a specified GitLab user is following, including their IDs, usernames, names, and profile information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"/users/{user_id}/following"
    url = base_url + endpoint
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_user_following(user_id=2330)
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