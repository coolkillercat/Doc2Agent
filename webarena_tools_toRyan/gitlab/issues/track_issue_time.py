import requests, json
from urllib.parse import quote



def track_issue_time(project_id: str, issue_iid: int, action: str, duration: str = None, summary: str = None):
    """
    Manages time tracking for GitLab issues. Supports setting time estimates, adding spent time, and resetting time values. Returns time tracking statistics in both human-readable and seconds format.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        issue_iid (int): The internal ID of the issue.
        action (str): Action to perform: 'estimate', 'reset_estimate', 'add_spent', 'reset_spent', or 'get_stats'.
        duration (str, optional): Human-readable time duration (e.g., '3h30m'). Required for 'estimate' and 'add_spent'.
        summary (str, optional): A summary of how time was spent. Only used with 'add_spent'.
    
    Returns:
        Returns time tracking statistics for an issue, including estimated and spent time in both seconds and human-readable formats."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct the endpoint based on the action
    if action == 'estimate':
        endpoint = f"/projects/{project_id}/issues/{issue_iid}/time_estimate"
        params = {'duration': duration}
        method = 'POST'
    elif action == 'reset_estimate':
        endpoint = f"/projects/{project_id}/issues/{issue_iid}/reset_time_estimate"
        params = {}
        method = 'POST'
    elif action == 'add_spent':
        endpoint = f"/projects/{project_id}/issues/{issue_iid}/add_spent_time"
        params = {'duration': duration}
        if summary:
            params['summary'] = summary
        method = 'POST'
    elif action == 'reset_spent':
        endpoint = f"/projects/{project_id}/issues/{issue_iid}/reset_spent_time"
        params = {}
        method = 'POST'
    elif action == 'get_stats':
        endpoint = f"/projects/{project_id}/issues/{issue_iid}/time_stats"
        params = {}
        method = 'GET'
    else:
        raise ValueError(f"Invalid action: {action}. Must be one of: 'estimate', 'reset_estimate', 'add_spent', 'reset_spent', 'get_stats'")
    
    url = f"{base_url}{endpoint}"
    
    if method == 'GET':
        response = requests.get(url, headers=headers, params=params)
    else:
        response = requests.post(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = track_issue_time(project_id="183", issue_iid=1, action="get_stats")
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