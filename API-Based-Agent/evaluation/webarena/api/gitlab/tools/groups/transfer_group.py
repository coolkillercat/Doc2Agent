import requests, json
from urllib.parse import quote

def transfer_group(group_id: int, new_parent_group_id: int = None):
    """
    Transfers a group to a new parent group or turns a subgroup into a top-level group. This allows for restructuring of group hierarchies and organization of projects.
    
    Args:
        group_id (int): ID of the group to transfer
        new_parent_group_id (int, optional): ID of the new parent group. When not specified, the group to transfer is turned into a top-level group.
    
    Returns:
        Response: The HTTP response object from the API request
        
    Example:
        # Transfer group 183 to parent group 2330
        response = transfer_group(group_id=183, new_parent_group_id=2330)
        
        # Turn a subgroup into a top-level group
        response = transfer_group(group_id=183)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"/groups/{group_id}/transfer"
    
    url = base_url + endpoint
    
    params = {}
    if new_parent_group_id is not None:
        params['group_id'] = new_parent_group_id
    
    response = requests.post(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = transfer_group(group_id=183, new_parent_group_id=2330)
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