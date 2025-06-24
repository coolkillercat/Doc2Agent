import requests
from urllib.parse import quote

def list_billable_member_memberships(group_id, user_id, page=1, per_page=20):
    """
    Lists all projects and groups a billable user is a member of within a specified group hierarchy.
    
    This API endpoint works on top-level groups only and requires permission to administer 
    memberships for the group. The response represents only direct memberships.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group owned by the authenticated user
        user_id (int or str): The user ID of the billable member
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of items per page. Defaults to 20.
        
    Returns:
        requests.Response: The API response containing membership information
        
    Example:
        >>> response = list_billable_member_memberships(group_id=183, user_id=2330)
        >>> memberships = response.json()
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Ensure the group_id is properly URL-encoded if it's a string path
    encoded_group_id = quote(str(group_id), safe='')
    
    url = f"{base_url}/groups/{encoded_group_id}/billable_members/{user_id}/memberships"
    params = {
        'page': page,
        'per_page': per_page
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_billable_member_memberships(group_id=183, user_id=2330)
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