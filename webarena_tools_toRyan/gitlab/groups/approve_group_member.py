import requests, json
from urllib.parse import quote

def approve_group_member(group_id: str, member_id: int, base_url: str = None, token: str = None) -> dict:
    """
    Approves a pending user for a group, its subgroups, and projects. This converts a pending membership to an active membership, giving the user access to group resources.
    
    Args:
        group_id (str): The ID or URL-encoded path of the root group
        member_id (int): The ID of the member to approve
        base_url (str, optional): The base URL for the GitLab API. Defaults to configured URL.
        token (str, optional): The private token for authentication. Defaults to configured token.
    
    Returns:
        dict: Response from the API
        
    Example:
        >>> approve_group_member(group_id='183', member_id=2330)
        {'id': 2330, 'username': 'byteblaze', ...}
    """
    if base_url is None:
        base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    if token is None:
        token = 'GITLAB_KEY_REMOVED'
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    
    # URL encode the group_id if it's a path
    if not str(group_id).isdigit():
        group_id = quote(group_id, safe='')
    
    url = f"{base_url}/groups/{group_id}/members/{member_id}/approve"
    
    response = requests.put(url, headers=headers)
    return response

if __name__ == '__main__':
    r = approve_group_member(group_id='183', member_id=2330)
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