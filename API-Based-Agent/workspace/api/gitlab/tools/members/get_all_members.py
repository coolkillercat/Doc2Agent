import requests, json
from urllib.parse import quote

def get_all_members(id: str, entity_type: str = 'group', query: str = None, user_ids: list = None, show_seat_info: bool = False, state: str = None, page: int = 1, per_page: int = 20):
    """
    Retrieves a comprehensive list of members for a GitLab group or project, including inherited members, invited users, and members with permissions through ancestor groups. Allows filtering by query string, user IDs, and member state.
    
    Args:
        id (str): The ID or URL-encoded path of the project or group
        entity_type (str): Type of entity - 'group' or 'project'
        query (str, optional): A query string to search for members
        user_ids (list, optional): Filter the results on the given user IDs
        show_seat_info (bool, optional): Show seat information for users
        state (str, optional): Filter results by member state, one of 'awaiting' or 'active'
        page (int, optional): Page number for pagination
        per_page (int, optional): Number of items per page
        
    Returns:
        Returns a comprehensive list of group or project members including inherited members, invited users, and members with permissions through ancestor groups, with their access levels and account details."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Determine the correct endpoint based on entity_type
    if entity_type.lower() == 'group':
        endpoint = f"{base_url}/groups/{quote(str(id), safe='')}/members/all"
    else:
        endpoint = f"{base_url}/projects/{quote(str(id), safe='')}/members/all"
    
    # Build query parameters
    params = {
        'page': page,
        'per_page': per_page
    }
    
    if query:
        params['query'] = query
    
    if user_ids:
        params['user_ids'] = user_ids
    
    if show_seat_info:
        params['show_seat_info'] = show_seat_info
    
    if state:
        params['state'] = state
    
    # Make the API request
    response = requests.get(endpoint, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_all_members(id=183, entity_type='project', per_page=10)
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