import requests, json
from urllib.parse import quote

def get_user_contributed_projects(user_id: str, order_by: str = 'created_at', simple: bool = False, sort: str = 'desc'):
    """
    Retrieves a list of projects that a specific user has contributed to. The results can be customized by ordering and sorting preferences to help analyze a user's project involvement history.
    
    Args:
        user_id (str): The ID or username of the user.
        order_by (str, optional): Return projects ordered by 'id', 'name', 'path', 'created_at', 'updated_at', or 'last_activity_at'. Defaults to 'created_at'.
        simple (bool, optional): Return only limited fields for each project. Defaults to False.
        sort (str, optional): Return projects sorted in 'asc' or 'desc' order. Defaults to 'desc'.
        
    Returns:
        requests.Response: The API response containing the list of contributed projects.
        
    Example:
        >>> response = get_user_contributed_projects(user_id="2330")
        >>> response = get_user_contributed_projects(user_id="2330", order_by="name", simple=True, sort="asc")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Ensure user_id is properly URL encoded
    encoded_user_id = quote(str(user_id), safe='')
    
    # Build the URL with query parameters
    url = f"{base_url}/users/{encoded_user_id}/contributed_projects"
    
    params = {
        'order_by': order_by,
        'simple': simple,
        'sort': sort
    }
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_user_contributed_projects(user_id="2330", order_by="created_at", simple=False, sort="desc")
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