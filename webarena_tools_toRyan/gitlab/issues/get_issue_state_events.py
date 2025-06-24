import requests, json
from urllib.parse import quote



def get_issue_state_events(project_id: int, issue_iid: int, sort: str = 'desc', pagination: tuple = (1, 20)) -> list:
    """
    Retrieves a chronological list of state changes for a specific issue in a project, showing when the issue was opened, closed, or reopened, by whom, and at what time. Useful for auditing issue lifecycle and accountability tracking.
    
    Args:
        project_id (int): The ID of the project containing the issue
        issue_iid (int): The internal ID of the issue
        sort (str, optional): Sort direction, either 'asc' or 'desc'. Defaults to 'desc'.
        pagination (tuple, optional): A tuple containing (page number, per_page). Defaults to (1, 20).
    
    Returns:
        Returns a chronological list of state changes for a specific issue, showing when it was opened, closed, or reopened, by whom, and at what time."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    page, per_page = pagination
    
    url = f"{base_url}/projects/{project_id}/issues/{issue_iid}/resource_state_events"
    
    params = {
        'sort': sort,
        'page': page,
        'per_page': per_page
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_issue_state_events(project_id=183, issue_iid=1)
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