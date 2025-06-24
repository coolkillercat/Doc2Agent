import requests
from urllib.parse import quote


def list_project_shareable_groups(project_id, search=None, base_url=None, token=None):
    """
    Retrieves a list of groups that can be shared with a specific project. Optionally filters the results based on a search term.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project.
        search (str, optional): Optional search term to filter groups.
        base_url (str, optional): The base URL for the GitLab API.
        token (str, optional): The private token for authentication.
        
    Returns:
        Response object from the API request.
        
    Example:
        >>> list_project_shareable_groups(183)
        >>> list_project_shareable_groups(183, search="git")
        >>> list_project_shareable_groups("group/project", search="gitlab")
    """
    if base_url is None:
        base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    if token is None:
        token = "GITLAB_KEY_REMOVED"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    
    # URL encode the project_id if it's a string path
    if not str(project_id).isdigit():
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/share_locations"
    
    params = {}
    if search:
        params['search'] = search
    
    response = requests.get(url, headers=headers, params=params)
    return response


if __name__ == '__main__':
    r = list_project_shareable_groups(project_id=183, search="git")
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