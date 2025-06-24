import requests, json
from urllib.parse import quote

def clone_issue(project_id: str, issue_iid: int, to_project_id: int, with_notes: bool = False):
    """
    Clones an issue from one project to another, copying data such as labels, milestones, and optionally notes.
    
    Args:
        project_id (str): ID or URL-encoded path of the source project
        issue_iid (int): Internal ID of the issue to clone
        to_project_id (int): ID of the target project where the issue will be cloned
        with_notes (bool, optional): Whether to include notes in the cloned issue. Defaults to False.
    
    Returns:
        Response: API response containing the newly created issue details
    
    Example:
        >>> clone_issue(project_id=183, issue_iid=1, to_project_id=183, with_notes=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/issues/{issue_iid}/clone"
    
    params = {
        'to_project_id': to_project_id,
        'with_notes': with_notes
    }
    
    response = requests.post(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = clone_issue(project_id=183, issue_iid=1, to_project_id=183, with_notes=True)
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