import requests, json
from urllib.parse import quote



def get_group_or_project_invitations(id: str, is_group: bool = True, query: str = None, page: int = 1, per_page: int = 20) -> requests.Response:
    """
    Retrieves pending invitations for a GitLab group or project. Allows filtering by email and supports pagination to manage results for groups or projects with many pending invitations.
    
    Args:
        id (str): The ID or URL-encoded path of the project or group
        is_group (bool): Whether the ID refers to a group (True) or a project (False)
        query (str, optional): A query string to search for invited members by invite email
        page (int, optional): Page to retrieve (default: 1)
        per_page (int, optional): Number of member invitations to return per page (default: 20)
        
    Returns:
        Returns a list of pending invitations for a GitLab group or project with details about each invitation including access level, email, and creator information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Determine the endpoint based on whether we're querying a group or project
    resource_type = "groups" if is_group else "projects"
    
    # Build the URL with query parameters
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/{resource_type}/{id}/invitations"
    
    # Set up query parameters
    params = {
        'page': page,
        'per_page': per_page
    }
    
    # Add query parameter if provided
    if query:
        params['query'] = query
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_group_or_project_invitations(id="183", is_group=False)
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