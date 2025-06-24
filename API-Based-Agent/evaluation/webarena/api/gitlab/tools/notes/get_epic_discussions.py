import requests
from urllib.parse import quote


def get_epic_discussions(group_id, epic_id):
    """
    Retrieves all discussion threads and comments for a specific epic in a group, providing a comprehensive view of the epic's conversation history.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group
        epic_id (int): The ID of the epic
        
    Returns:
        requests.Response: The API response containing all discussion items for the epic
        
    Example:
        >>> response = get_epic_discussions(group_id="my-group", epic_id=123)
        >>> response = get_epic_discussions(group_id=5, epic_id=11)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Encode the group_id if it's a path
    if not str(group_id).isdigit():
        group_id = quote(str(group_id), safe='')
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{group_id}/epics/{epic_id}/discussions"
    
    response = requests.get(url, headers=headers)
    return response


if __name__ == '__main__':
    r = get_epic_discussions(group_id=183, epic_id=1)
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