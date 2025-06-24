import requests, json
from urllib.parse import quote



def get_todo_items(state: str = None, action: str = None, target_type: str = None, sort: str = 'created_desc', per_page: int = 20, page: int = 1):
    """
    Retrieves a user's to-do items from GitLab with optional filtering by state, action type, and target object type. Results can be sorted and paginated as needed.
    
    Args:
        state (str, optional): Filter by to-do state. Can be 'pending' or 'done'. Defaults to None.
        action (str, optional): Filter by to-do action type. Defaults to None.
        target_type (str, optional): Filter by the target type of to-do. Defaults to None.
        sort (str, optional): Sort by criteria. Possible values: created_at, created_desc. Defaults to 'created_desc'.
        per_page (int, optional): Number of items per page. Defaults to 20.
        page (int, optional): Page number. Defaults to 1.
        
    Returns:
        Returns a user's to-do items from GitLab with details about each item including project information, author, action type, target, and current state."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/todos"
    
    params = {
        'per_page': per_page,
        'page': page,
        'sort': sort
    }
    
    if state:
        params['state'] = state
    if action:
        params['action'] = action
    if target_type:
        params['target_type'] = target_type
    
    response = requests.get(base_url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_todo_items(per_page=5, state='pending')
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