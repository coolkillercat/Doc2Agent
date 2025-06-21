import requests, json
from urllib.parse import quote


def move_issue(source_project_id: str, issue_iid: int, to_project_id: int):
    """
    Moves an issue from its current project to a different project, transferring all relevant metadata like labels and milestones with matching names. Returns the moved issue with updated information.
    
    Args:
        source_project_id (str): The ID or URL-encoded path of the project containing the issue
        issue_iid (int): The internal ID of the issue to be moved
        to_project_id (int): The ID of the target project where the issue will be moved to
        
    Returns:
        Returns the complete details of an issue after moving it from one project to another, including its metadata, assignees, time statistics, and references."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{source_project_id}/issues/{issue_iid}/move"
    
    data = {
        'to_project_id': to_project_id
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = move_issue(source_project_id=183, issue_iid=1, to_project_id=184)
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