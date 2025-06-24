import requests, json
from urllib.parse import quote



def get_user_followers(user_id: int) -> list:
    """
    Retrieve a list of users who are following the specified GitLab user. Returns follower details including ID, name, username, and profile information.
    
    Args:
        user_id (int): The ID of the GitLab user whose followers to retrieve
        
    Returns:
        Returns a list of users who are following a specified GitLab user, including their profile information such as ID, username, name, and avatar URL."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/users/{user_id}/followers"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_user_followers(user_id=2330)
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