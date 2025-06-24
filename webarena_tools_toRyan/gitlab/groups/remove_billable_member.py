import requests, json
from urllib.parse import quote


def remove_billable_member(group_id: str, user_id: int) -> requests.Response:
    """
    Removes a billable member from a group, its subgroups, and projects. This is useful for managing group membership when a user has been added directly to projects within the group but needs to be completely removed from billing.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        user_id (int): The user ID of the member to remove
        
    Returns:
        requests.Response: The response from the API
        
    Example:
        >>> response = remove_billable_member(group_id="183", user_id=2330)
        >>> print(response.status_code)
        204
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{quote(str(group_id))}/billable_members/{user_id}"
    
    response = requests.delete(url, headers=headers)
    return response

if __name__ == '__main__':
    r = remove_billable_member(group_id="183", user_id=2330)
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