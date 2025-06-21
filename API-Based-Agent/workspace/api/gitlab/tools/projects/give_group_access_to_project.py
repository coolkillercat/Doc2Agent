import requests, json
from urllib.parse import quote

def give_group_access_to_project(project_id:int, group_id:int, access_level:str='developer', expires_at:str=None, group_access:int=None):
    """
    Grants a specific group access to a GitLab project with specified permissions. This allows teams or departments to collaborate on projects with appropriate access controls.
    
    Args:
        project_id (int): The ID of the project to share with the group
        group_id (int): The ID of the group to share with
        access_level (str, optional): The access level to grant the group. Defaults to 'developer'.
            Valid values: 'no access', 'minimal', 'guest', 'reporter', 'developer', 'maintainer', 'owner'
        expires_at (str, optional): Share expiration date in ISO 8601 format: 2016-09-26. Defaults to None.
        group_access (int, optional): Access level as integer value. Defaults to None.
            Valid values: 0, 5, 10, 20, 30, 40, 50
    
    Returns:
        requests.Response: The API response object
    
    Examples:
        >>> give_group_access_to_project(183, 12, 'developer')
        >>> give_group_access_to_project(183, 12, group_access=30)
        >>> give_group_access_to_project(183, 12, 'maintainer', expires_at='2025-12-31')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/share"
    
    data = {
        "group_id": group_id
    }
    
    # If group_access is not provided, use access_level
    if group_access is None:
        access_levels = {
            'no access': 0,
            'minimal': 5,
            'guest': 10,
            'reporter': 20,
            'developer': 30,
            'maintainer': 40,
            'owner': 50
        }
        data["group_access"] = access_levels.get(access_level.lower(), 30)  # Default to developer if not found
    else:
        data["group_access"] = group_access
    
    if expires_at:
        data["expires_at"] = expires_at
    
    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = give_group_access_to_project(project_id=183, group_id=12, access_level='developer')
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