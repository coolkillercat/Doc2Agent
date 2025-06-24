import requests
from urllib.parse import quote

def get_billable_members(group_id, search=None, sort=None, page=1, per_page=20):
    """
    Retrieves a list of billable members for a top-level group including members in subgroups and projects.
    
    This API endpoint works on top-level groups only. It does not work on subgroups.
    
    Args:
        group_id (int/str): The ID or URL-encoded path of the group owned by the authenticated user
        search (str, optional): A query string to search for group members by name, username, or public email
        sort (str, optional): Sort attribute and order. Supported values include:
                             'access_level_asc', 'access_level_desc', 'last_joined', 'name_asc',
                             'name_desc', 'oldest_joined', 'oldest_sign_in', 'recent_sign_in',
                             'last_activity_on_asc', 'last_activity_on_desc'
        page (int, optional): The page number for pagination. Defaults to 1.
        per_page (int, optional): The number of results per page for pagination. Defaults to 20.
        
    Returns:
        Response: The API response containing billable group members
        
    Example:
        >>> get_billable_members(183)
        >>> get_billable_members(183, search="byteblaze", sort="name_asc", page=1, per_page=10)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_group_id = quote(str(group_id), safe='')
    url = f"{base_url}/groups/{encoded_group_id}/billable_members"
    
    params = {
        'page': page,
        'per_page': per_page
    }
    
    if search:
        params['search'] = search
    
    if sort:
        params['sort'] = sort
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_billable_members(group_id=183, search="byteblaze", sort="name_asc", page=1, per_page=10)
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