import requests, json
from urllib.parse import quote



def list_project_groups(project_id: str, search: str = None, shared_min_access_level: int = None, shared_visible_only: bool = None, skip_groups: list = None, with_shared: bool = False):
    """
    Retrieves a list of ancestor groups for a specific project. This helps users understand the organizational hierarchy and group relationships for a given project.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        search (str, optional): Search for specific groups
        shared_min_access_level (int, optional): Limit to shared groups with at least this role (access_level)
        shared_visible_only (bool, optional): Limit to shared groups user has access to
        skip_groups (list, optional): Skip the group IDs passed
        with_shared (bool, optional): Include projects shared with this group. Default is False
        
    Returns:
        Retrieves a list of ancestor groups for a specific project, showing the organizational hierarchy and group relationships."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct the URL with the project ID
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/groups"
    
    # Prepare query parameters
    params = {}
    if search:
        params['search'] = search
    if shared_min_access_level is not None:
        params['shared_min_access_level'] = shared_min_access_level
    if shared_visible_only is not None:
        params['shared_visible_only'] = shared_visible_only
    if skip_groups:
        params['skip_groups'] = skip_groups
    if with_shared:
        params['with_shared'] = with_shared
    
    # Make the API request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = list_project_groups(project_id=183)
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