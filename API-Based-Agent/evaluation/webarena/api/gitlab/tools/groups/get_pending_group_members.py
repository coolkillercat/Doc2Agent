import requests
from urllib.parse import quote

def get_pending_group_members(group_id: str, page: int = 1, per_page: int = 20):
    """
    Retrieves a list of all pending members (awaiting state or invited without GitLab account) for a top-level group and its subgroups and projects. This helps administrators review and manage outstanding membership invitations and approvals.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of items per page. Defaults to 20.
        
    Returns:
        Response: The API response containing pending group members
        
    Example:
        >>> get_pending_group_members('2330')
        >>> get_pending_group_members(2330, page=2, per_page=10)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_group_id = quote(str(group_id), safe='')
    url = f"{base_url}/groups/{encoded_group_id}/pending_members"
    
    params = {
        'page': page,
        'per_page': per_page
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_pending_group_members(group_id=2330, page=1, per_page=20)
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