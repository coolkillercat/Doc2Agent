import requests, json
from urllib.parse import quote

def share_project_with_group(project_id, group_id, group_access, expires_at=None, base_url="http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token="glpat-qvQ-N6mN_tAddXb2WWdi"):
    """
    Shares a project with a specific group by granting them a defined access level. Optionally allows setting an expiration date for the shared access.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        group_id (int): The ID of the group to share with
        group_access (int): The role (access_level) to grant the group
        expires_at (str, optional): Share expiration date in ISO 8601 format (e.g., '2023-12-31')
        base_url (str, optional): The base URL of the GitLab API
        token (str, optional): The private token for authentication
    
    Returns:
        Response: The HTTP response from the API
        
    Example:
        >>> share_project_with_group(project_id=183, group_id=42, group_access=30)
        >>> share_project_with_group(project_id=183, group_id=42, group_access=30, expires_at='2023-12-31')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    
    # Handle both integer and string project IDs
    if isinstance(project_id, str) and not project_id.isdigit():
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/share"
    
    payload = {
        "group_id": group_id,
        "group_access": group_access
    }
    
    if expires_at:
        payload["expires_at"] = expires_at
    
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = share_project_with_group(project_id=183, group_id=42, group_access=30)
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