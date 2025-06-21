import requests, json
from urllib.parse import quote

def get_group_members(group_id: str, skip_users: bool = False, all_available: bool = False, 
                      search: str = None, per_page: int = 20, page: int = 1) -> list:
    """
    Retrieves all members of a specified group. This function helps in managing group composition and understanding team structure.
    
    Args:
        group_id (str): The ID of the group to retrieve members from
        skip_users (bool, optional): Skip users and return only groups. Defaults to False.
        all_available (bool, optional): Show all available users and groups. Defaults to False.
        search (str, optional): Search for specific members. Defaults to None.
        per_page (int, optional): Number of items to list per page. Defaults to 20.
        page (int, optional): Page number of the results to fetch. Defaults to 1.
        
    Returns:
        list: A list of group members with their details
        
    Example:
        >>> get_group_members("183")
        [{'id': 123, 'username': 'user1', ...}, {'id': 456, 'username': 'user2', ...}]
        
        >>> get_group_members("183", search="john", per_page=10)
        [{'id': 789, 'username': 'john_doe', ...}]
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(str(group_id), safe='')}/members"
    
    params = {}
    if skip_users:
        params['skip_users'] = skip_users
    if all_available:
        params['all_available'] = all_available
    if search:
        params['search'] = search
    if per_page:
        params['per_page'] = per_page
    if page:
        params['page'] = page
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    return response

if __name__ == '__main__':
    r = get_group_members(group_id="183")
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