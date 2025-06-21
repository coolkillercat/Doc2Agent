import requests, json
from urllib.parse import quote

def add_member_to_group_or_project(id: str, user_id: str, access_level: int, location_type: str = 'group', expires_at: str = None, member_role_id: int = None, invite_source: str = None):
    """
    Adds a user as a member to a GitLab group or project with specified access level and optional expiration date.
    
    Args:
        id (str): The ID or URL-encoded path of the project or group
        user_id (str): The user ID of the new member or multiple IDs separated by commas
        access_level (int): A valid access level (e.g., 10=Guest, 20=Reporter, 30=Developer, 40=Maintainer, 50=Owner)
        location_type (str, optional): Type of entity to add member to ('group' or 'project'). Defaults to 'group'.
        expires_at (str, optional): A date string in the format YEAR-MONTH-DAY. Defaults to None.
        member_role_id (int, optional): The ID of a member role. Ultimate only. Defaults to None.
        invite_source (str, optional): The source of the invitation. Defaults to None.
        
    Returns:
        Response: HTTP response from the API
        
    Example:
        >>> add_member_to_group_or_project(id='183', user_id='2330', access_level=30, location_type='project')
        <Response [201]>
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Determine whether to add to a group or project
    if location_type.lower() == 'group':
        url = f"{base_url}/groups/{quote(str(id), safe='')}/members"
    else:
        url = f"{base_url}/projects/{quote(str(id), safe='')}/members"
    
    # Build payload with required and optional parameters
    payload = {
        "user_id": user_id,
        "access_level": access_level
    }
    
    # Add optional parameters if provided
    if expires_at:
        payload["expires_at"] = expires_at
    if member_role_id:
        payload["member_role_id"] = member_role_id
    if invite_source:
        payload["invite_source"] = invite_source
    
    # Make the POST request to add the member
    response = requests.post(url, headers=headers, json=payload)
    
    return response

if __name__ == '__main__':
    r = add_member_to_group_or_project(id='183', user_id='2330', access_level=30, location_type='project')
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