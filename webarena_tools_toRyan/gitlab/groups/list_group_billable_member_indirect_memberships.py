import requests
from urllib.parse import quote

def list_group_billable_member_indirect_memberships(group_id, user_id, page=1, per_page=20):
    """
    Retrieves all indirect memberships for a billable member of a top-level group. This helps identify which projects and groups a user is a member of that have been invited to the requested root group.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group
        user_id (int): The user ID of the billable member
        page (int, optional): The page number for pagination. Defaults to 1.
        per_page (int, optional): Number of items per page. Defaults to 20.
        
    Returns:
        requests.Response: The API response
        
    Example:
        >>> list_group_billable_member_indirect_memberships(group_id=183, user_id=2330)
        >>> list_group_billable_member_indirect_memberships(group_id="my-group", user_id=2330, page=2, per_page=50)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Encode group_id if it's a path
    if not str(group_id).isdigit():
        group_id = quote(str(group_id), safe='')
    
    url = f"{base_url}/groups/{group_id}/billable_members/{user_id}/indirect"
    
    params = {
        'page': page,
        'per_page': per_page
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = list_group_billable_member_indirect_memberships(group_id=183, user_id=2330)
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