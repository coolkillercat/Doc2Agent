import requests, json
from urllib.parse import quote



def get_members(id: str, resource_type: str = 'group', query: str = None, user_ids: list = None, skip_users: list = None, show_seat_info: bool = False, page: int = 1, per_page: int = 20):
    """
    Retrieves a list of members from a GitLab group or project.
    
    Args:
        id: The ID or URL-encoded path of the project or group
        resource_type: Type of resource - 'group' or 'project'
        query: A query string to search for members
        user_ids: Filter the results on the given user IDs
        skip_users: Filter skipped users out of the results
        show_seat_info: Show seat information for users
        page: Page number for pagination
        per_page: Number of items per page
        
    Returns:
        Returns a list of members from a GitLab group or project with their user details and access information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Determine the endpoint based on resource_type
    if resource_type.lower() == 'group':
        endpoint = f"/groups/{quote(str(id), safe='')}/members"
    elif resource_type.lower() == 'project':
        endpoint = f"/projects/{quote(str(id), safe='')}/members"
    else:
        raise ValueError("resource_type must be either 'group' or 'project'")
    
    # Prepare the base URL
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}{endpoint}"
    
    # Prepare query parameters
    params = {
        'page': page,
        'per_page': per_page
    }
    
    if query:
        params['query'] = query
    
    if user_ids:
        params['user_ids'] = user_ids
    
    if skip_users:
        params['skip_users'] = skip_users
    
    if show_seat_info:
        params['show_seat_info'] = show_seat_info
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_members(id=183, resource_type='project', per_page=10)
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