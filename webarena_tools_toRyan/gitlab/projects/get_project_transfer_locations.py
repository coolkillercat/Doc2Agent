import requests, json
from urllib.parse import quote



def get_project_transfer_locations(project_id: str, search: str = None):
    """
    Retrieves a list of groups to which the authenticated user can transfer a specific project. This helps project administrators find suitable target groups when they need to relocate a project within the organization.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        search (str, optional): The group names to search for.
    
    Returns:
        Returns a list of groups to which the authenticated user can transfer a specific project."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL-encode the project_id if it's not numeric
    if not str(project_id).isdigit():
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/transfer_locations"
    
    # Add search parameter if provided
    params = {}
    if search:
        params['search'] = search
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_transfer_locations(project_id=183)
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