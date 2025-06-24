import requests
from urllib.parse import quote

def restore_group(group_id: str) -> dict:
    """
    Restores a group that was previously marked for deletion. This allows administrators to recover a group and all its contents before permanent deletion occurs.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group to restore
        
    Returns:
        dict: Response from the API as a dictionary
        
    Example:
        >>> restore_group(group_id="183")
        {'id': 183, 'name': 'Group Name', ...}
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    url = f"{base_url}/groups/{quote(str(group_id), safe='')}/restore"
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    return response

if __name__ == '__main__':
    r = restore_group(group_id="183")
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