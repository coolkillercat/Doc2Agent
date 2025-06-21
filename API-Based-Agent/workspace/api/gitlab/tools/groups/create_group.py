import requests, json
from urllib.parse import quote



def create_group(name: str, path: str, description: str = None, visibility: str = None, parent_id: int = None, project_creation_level: str = None, subgroup_creation_level: str = None, require_two_factor_authentication: bool = None, two_factor_grace_period: int = None, auto_devops_enabled: bool = None, emails_enabled: bool = None, lfs_enabled: bool = None, request_access_enabled: bool = None, default_branch: str = None, wiki_access_level: str = None):
    """
    Creates a new project group in GitLab with customizable settings for visibility, permissions, and features. Allows for creation of both top-level groups and nested subgroups with specific access controls.
    
    Args:
        name (str): The name of the group
        path (str): The path of the group
        description (str, optional): The group's description
        visibility (str, optional): The group's visibility. Can be 'private', 'internal', or 'public'
        parent_id (int, optional): The parent group ID for creating nested group
        project_creation_level (str, optional): Determine if developers can create projects in the group
        subgroup_creation_level (str, optional): Allowed to create subgroups
        require_two_factor_authentication (bool, optional): Require all users in this group to set up two-factor authentication
        two_factor_grace_period (int, optional): Time before Two-factor authentication is enforced (in hours)
        auto_devops_enabled (bool, optional): Default to Auto DevOps pipeline for all projects within this group
        emails_enabled (bool, optional): Enable email notifications
        lfs_enabled (bool, optional): Enable/disable Large File Storage (LFS) for the projects in this group
        request_access_enabled (bool, optional): Allow users to request member access
        default_branch (str, optional): The default branch name for group's projects
        wiki_access_level (str, optional): The wiki access level. Can be 'disabled', 'private', or 'enabled'
        
    Returns:
        Returns details about a newly created GitLab group including its ID, name, path, visibility settings, and configuration options."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups"
    
    payload = {
        'name': name,
        'path': path
    }
    
    # Add optional parameters if provided
    if description is not None:
        payload['description'] = description
    if visibility is not None:
        payload['visibility'] = visibility
    if parent_id is not None:
        payload['parent_id'] = parent_id
    if project_creation_level is not None:
        payload['project_creation_level'] = project_creation_level
    if subgroup_creation_level is not None:
        payload['subgroup_creation_level'] = subgroup_creation_level
    if require_two_factor_authentication is not None:
        payload['require_two_factor_authentication'] = require_two_factor_authentication
    if two_factor_grace_period is not None:
        payload['two_factor_grace_period'] = two_factor_grace_period
    if auto_devops_enabled is not None:
        payload['auto_devops_enabled'] = auto_devops_enabled
    if emails_enabled is not None:
        payload['emails_enabled'] = emails_enabled
    if lfs_enabled is not None:
        payload['lfs_enabled'] = lfs_enabled
    if request_access_enabled is not None:
        payload['request_access_enabled'] = request_access_enabled
    if default_branch is not None:
        payload['default_branch'] = default_branch
    if wiki_access_level is not None:
        payload['wiki_access_level'] = wiki_access_level
    
    response = requests.post(url, headers=headers, json=payload)
    
    return response

if __name__ == '__main__':
    r = create_group(name="Test Group", path="test-group", description="This is a test group", visibility="private")
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