import requests, json
from urllib.parse import quote



def get_todos(action: str = None, author_id: int = None, project_id: int = None, group_id: int = None, state: str = None, type: str = None):
    """
    Retrieves to-do items for the current user with optional filtering options to narrow down results by action, author, project, group, state or type of to-do item.
    
    Args:
        action (str, optional): The action to be filtered. Can be 'assigned', 'mentioned', 'build_failed', etc.
        author_id (int, optional): The ID of an author.
        project_id (int, optional): The ID of a project.
        group_id (int, optional): The ID of a group.
        state (str, optional): The state of the to-do item. Can be either 'pending' or 'done'.
        type (str, optional): The type of to-do item. Can be 'Issue', 'MergeRequest', 'Commit', etc.
        
    Returns:
        Returns a list of to-do items for the current user with details about each item including project information, author, action type, target, and status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = "/todos"
    
    params = {}
    if action:
        params['action'] = action
    if author_id:
        params['author_id'] = author_id
    if project_id:
        params['project_id'] = project_id
    if group_id:
        params['group_id'] = group_id
    if state:
        params['state'] = state
    if type:
        params['type'] = type
    
    url = base_url + endpoint
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_todos(project_id=183, state='pending')
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