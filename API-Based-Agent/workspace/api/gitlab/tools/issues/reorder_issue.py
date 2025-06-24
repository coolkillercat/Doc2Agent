import requests, json
from urllib.parse import quote

def reorder_issue(project_id: str, issue_iid: int, move_after_id: int = None, move_before_id: int = None):
    """
    Reorders an issue in a project's issue list for manual sorting purposes. The issue can be positioned relative to other issues by specifying either the issue that should come before it, after it, or both.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the project's issue
        move_after_id (int, optional): The global ID of a project's issue that should be placed after this issue
        move_before_id (int, optional): The global ID of a project's issue that should be placed before this issue
        
    Returns:
        requests.Response: The API response
        
    Example:
        >>> reorder_issue(project_id=183, issue_iid=1, move_after_id=2)
        >>> reorder_issue(project_id=183, issue_iid=1, move_before_id=3)
        >>> reorder_issue(project_id=183, issue_iid=1, move_after_id=2, move_before_id=3)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/issues/{issue_iid}/reorder"
    
    params = {}
    if move_after_id is not None:
        params['move_after_id'] = move_after_id
    if move_before_id is not None:
        params['move_before_id'] = move_before_id
    
    response = requests.put(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = reorder_issue(project_id=183, issue_iid=1, move_after_id=2, move_before_id=3)
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