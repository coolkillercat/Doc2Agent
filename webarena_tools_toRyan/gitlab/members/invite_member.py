import requests, json
from urllib.parse import quote



def invite_member(id: str, access_level: int, email: str = None, user_id: int = None, expires_at: str = None, invite_source: str = None, member_role_id: int = None, target_type: str = 'group'):
    """
    Invites a user to join a GitLab group or project by email or user ID. This function allows you to set appropriate access levels and optional expiration dates for the new member.
    
    Args:
        id (str): The ID of the project or group to add the member to.
        access_level (int): A valid access level for the new member.
        email (str, optional): The email of the new member. Required if user_id is not provided.
        user_id (int, optional): The ID of the new member. Required if email is not provided.
        expires_at (str, optional): A date string in the format YEAR-MONTH-DAY.
        invite_source (str, optional): The source of the invitation.
        member_role_id (int, optional): Assigns the new member to the provided custom role.
        target_type (str, optional): Whether to add to a 'group' or 'project'. Default is 'group'.
        
    Returns:
        Returns the status of a member invitation to a GitLab group or project."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Determine if adding to a group or project
    if target_type == 'group':
        endpoint = f"{base_url}/groups/{id}/invitations"
    else:
        endpoint = f"{base_url}/projects/{id}/invitations"
    
    # Prepare request data
    data = {'access_level': access_level}
    
    if email:
        data['email'] = email
    if user_id:
        data['user_id'] = user_id
    if expires_at:
        data['expires_at'] = expires_at
    if invite_source:
        data['invite_source'] = invite_source
    if member_role_id:
        data['member_role_id'] = member_role_id
        
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # Make the API request
    response = requests.post(endpoint, headers=headers, json=data)
    
    return response

if __name__ == '__main__':
    r = invite_member(id="183", access_level=30, email="test@example.com", target_type='project')
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