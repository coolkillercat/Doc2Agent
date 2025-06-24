import requests, json
from urllib.parse import quote


def list_provisioned_users(group_id, username=None, search=None, active=None, blocked=None, created_after=None, created_before=None):
    """
    Retrieves a list of users provisioned by a specific group. Enables filtering by username, activity status, creation dates, and search terms to help with user management and auditing.
    
    Args:
        group_id (int or str): ID or URL-encoded path of the group
        username (str, optional): Return single user with a specific username
        search (str, optional): Search users by name, email, username
        active (bool, optional): Return only active users
        blocked (bool, optional): Return only blocked users
        created_after (str, optional): Return users created after the specified time (datetime format)
        created_before (str, optional): Return users created before the specified time (datetime format)
    
    Returns:
        requests.Response: The API response containing the list of provisioned users
        
    Example:
        >>> response = list_provisioned_users(183)
        >>> response = list_provisioned_users(183, username="byteblaze")
        >>> response = list_provisioned_users(183, active=True, created_after="2023-01-01T00:00:00.000Z")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # Build base URL
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_group_id = quote(str(group_id), safe='')
    url = f"{base_url}/groups/{encoded_group_id}/provisioned_users"
    
    # Build query parameters
    params = {}
    if username is not None:
        params['username'] = username
    if search is not None:
        params['search'] = search
    if active is not None:
        params['active'] = active
    if blocked is not None:
        params['blocked'] = blocked
    if created_after is not None:
        params['created_after'] = created_after
    if created_before is not None:
        params['created_before'] = created_before
    
    # Make the API request
    response = requests.get(url, headers=headers, params=params)
    
    return response


if __name__ == '__main__':
    r = list_provisioned_users(group_id=183)
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