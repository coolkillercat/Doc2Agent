import requests, json
from urllib.parse import quote



def get_paginated_issues(page: int = 1, per_page: int = 20, group_id: str = None, project_id: str = None):
    """
    Retrieve a paginated list of issues from a GitLab group or project. Allows controlling page number and items per page to navigate through large issue collections.
    
    Args:
        page (int, optional): The page number to retrieve. Defaults to 1.
        per_page (int, optional): Number of items per page. Defaults to 20.
        group_id (str, optional): The ID of the group to get issues from. Defaults to None.
        project_id (str, optional): The ID of the project to get issues from. Defaults to None.
        
    Returns:
        Returns a paginated list of GitLab issues with detailed metadata from a specified group or project."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct URL based on whether we're fetching issues for a group or project
    if group_id:
        url = f"{base_url}/groups/{group_id}/issues"
    elif project_id:
        url = f"{base_url}/projects/{project_id}/issues"
    else:
        url = f"{base_url}/issues"
    
    # Add pagination parameters
    params = {
        'page': page,
        'per_page': per_page
    }
    
    # Make the API call
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_paginated_issues(page=1, per_page=5, project_id=183)
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