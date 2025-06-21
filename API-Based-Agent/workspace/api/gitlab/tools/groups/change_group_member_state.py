import requests, json
from urllib.parse import quote


def change_group_member_state(group_id: str, user_id: int, state: str, base_url: str = None, token: str = None):
    """
    Changes the membership state of a user in a group. The state is applied to all subgroups and projects.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group owned by the authenticated user.
        user_id (int): The user ID of the member.
        state (str): The new state for the user. Must be either 'awaiting' or 'active'.
        base_url (str, optional): The base URL for the GitLab API. Defaults to None.
        token (str, optional): The private token for authentication. Defaults to None.
        
    Returns:
        requests.Response: The API response object.
        
    Example:
        >>> change_group_member_state(group_id="183", user_id=2330, state="active")
        <Response [200]>
    """
    if base_url is None:
        base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    if token is None:
        token = "glpat-qvQ-N6mN_tAddXb2WWdi"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    
    encoded_group_id = quote(str(group_id), safe='')
    
    url = f"{base_url}/groups/{encoded_group_id}/members/{user_id}/state"
    params = {'state': state}
    
    response = requests.put(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = change_group_member_state(group_id="183", user_id=2330, state="active")
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