import requests, json
from urllib.parse import quote



def get_user_associations_count(user_id: int):
    """
    Retrieves counts of a user's associated projects, groups, issues, and merge requests. Useful for understanding a user's activity and contribution levels across the platform.
    
    Args:
        user_id (int): The ID of the user to retrieve associations count for
        
    Returns:
        Returns counts of a user's associated projects, groups, issues, and merge requests."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/users/{user_id}/associations_count"
    
    return requests.get(endpoint, headers=headers)

if __name__ == '__main__':
    r = get_user_associations_count(user_id=2330)
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