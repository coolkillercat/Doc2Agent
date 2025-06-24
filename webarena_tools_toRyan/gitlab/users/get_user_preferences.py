import requests, json
from urllib.parse import quote



def get_user_preferences() -> dict:
    """
    Retrieves the authenticated user's preferences including settings for viewing diffs, showing whitespace, and passing identities to CI JWT.

    Returns:
        Returns the authenticated user's preferences including settings for viewing diffs, showing whitespace, and identity passing options."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/user/preferences"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_user_preferences()
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