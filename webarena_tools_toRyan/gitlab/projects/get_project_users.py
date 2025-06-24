import requests, json
from urllib.parse import quote



def get_project_users(project_id: str, search: str = None, skip_users: list = None):
    """
    Retrieves a list of users who are members of a specific project. Supports filtering by search term and excluding specific users by ID.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        search (str, optional): Search for specific users. Defaults to None.
        skip_users (list, optional): Filter out users with the specified IDs. Defaults to None.
    
    Returns:
        Returns a list of users who are members of a specific project with their profile information and account status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Build the URL with the project ID
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/users"
    
    # Prepare query parameters
    params = {}
    if search:
        params['search'] = search
    if skip_users:
        params['skip_users'] = skip_users
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_project_users(project_id=183, search="byte", skip_users=[100, 101])
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