import requests
from urllib.parse import quote


def get_group_badges(group_id: str) -> dict:
    """
    Retrieves all badges associated with a specific group, enabling badge management and recognition systems within group contexts.
    
    Args:
        group_id (str): The ID of the group to get badges for
    
    Returns:
        dict: The API response containing group badges information
    
    Example:
        >>> get_group_badges(group_id="183")
        {'status_code': 200, 'badges': [...]}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(str(group_id))}/badges"
    response = requests.get(url, headers=headers)
    return response


if __name__ == '__main__':
    r = get_group_badges(group_id="183")
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