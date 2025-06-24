import requests, json
from urllib.parse import quote
from typing import Union, Dict, Any

def approve_all_pending_group_members(group_id: Union[int, str]) -> requests.Response:
    """
    Approves all pending users for a specified group and its subgroups and projects in one operation.
    Useful for quickly onboarding multiple team members to a group structure.
    
    Args:
        group_id (Union[int, str]): The ID or URL-encoded path of the root group owned by the authenticated user
        
    Returns:
        requests.Response: Response object from the API request
        
    Examples:
        >>> approve_all_pending_group_members(183)
        >>> approve_all_pending_group_members("my-group/subgroup")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL encode the group_id if it's a string path
    if isinstance(group_id, str) and '/' in group_id:
        group_id = quote(group_id, safe='')
    
    url = f"{base_url}/groups/{group_id}/members/approve_all"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = approve_all_pending_group_members(group_id=183)
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