import requests, json
from urllib.parse import quote



def get_project_events(project_id: str, action: str = None, target_type: str = None, before: str = None, after: str = None, sort: str = None, page: int = 1, per_page: int = 20) -> dict:
    """
    Retrieves events for a specific project with optional filtering by event type, target, and date range. Useful for activity monitoring, audit trails, and tracking project changes over time.
    
    Args:
        project_id (str): The ID of the project
        action (str, optional): Filter by action type. Defaults to None.
        target_type (str, optional): Filter by target type. Defaults to None.
        before (str, optional): Return events created before date (ISO 8601 format). Defaults to None.
        after (str, optional): Return events created after date (ISO 8601 format). Defaults to None.
        sort (str, optional): Sort events by 'asc' or 'desc'. Defaults to None.
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of events per page. Defaults to 20.
    
    Returns:
        Returns a list of events for a specific project with details including action type, target, author information, and timestamps."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/events"
    
    params = {
        'page': page,
        'per_page': per_page
    }
    
    if action:
        params['action'] = action
    if target_type:
        params['target_type'] = target_type
    if before:
        params['before'] = before
    if after:
        params['after'] = after
    if sort:
        params['sort'] = sort
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_events(project_id=183, per_page=5)
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