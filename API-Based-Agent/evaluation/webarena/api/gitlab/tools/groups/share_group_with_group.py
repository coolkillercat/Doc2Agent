import requests, json
from urllib.parse import quote


def share_group_with_group(group_id: str, target_group_id: int, access_level: int, expires_at: str = None):
    """
    Creates a link to share a group with another group, granting specific access permissions. 
    Allows organizations to establish group-to-group collaboration with controlled access levels 
    and optional expiration date.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group to be shared
        target_group_id (int): The ID of the group to share with
        access_level (int): The role (access_level) to grant the group
        expires_at (str, optional): Share expiration date in ISO 8601 format: 2016-09-26
    
    Returns:
        Response object with the result of the API call
        
    Example:
        >>> share_group_with_group(group_id='183', target_group_id=2330, access_level=30)
        >>> share_group_with_group(group_id='183', target_group_id=2330, access_level=30, expires_at='2025-06-12')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(str(group_id), safe='')}/share"
    
    payload = {
        "group_id": target_group_id,
        "group_access": access_level
    }
    
    if expires_at:
        payload["expires_at"] = expires_at
    
    response = requests.post(url, headers=headers, json=payload)
    return response


def unshare_group_with_group(group_id: str, target_group_id: int):
    """
    Deletes a link sharing a group with another group.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group that is being shared
        target_group_id (int): The ID of the group that was shared with
    
    Returns:
        Response object with the result of the API call
        
    Example:
        >>> unshare_group_with_group(group_id='183', target_group_id=2330)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(str(group_id), safe='')}/share/{target_group_id}"
    
    response = requests.delete(url, headers=headers)
    return response


if __name__ == '__main__':
    r = share_group_with_group(group_id='183', target_group_id=2330, access_level=30)
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