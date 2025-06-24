import requests, json
from urllib.parse import quote

def create_user_runner(runner_type: str, group_id: int = None, project_id: int = None, description: str = None, 
                       paused: bool = False, locked: bool = False, run_untagged: bool = True, tag_list: list = None, 
                       access_level: str = None, maximum_timeout: int = None, maintenance_note: str = None):
    """
    Creates a new runner linked to the current user with specified scope and configuration. 
    Returns the runner ID and authentication token that must be saved for future runner operations.
    
    Args:
        runner_type (str): Specifies the scope of the runner; 'instance_type', 'group_type', or 'project_type'.
        group_id (int, optional): The ID of the group that the runner is created in. Required if runner_type is 'group_type'.
        project_id (int, optional): The ID of the project that the runner is created in. Required if runner_type is 'project_type'.
        description (str, optional): Description of the runner.
        paused (bool, optional): Specifies if the runner should ignore new jobs. Default is False.
        locked (bool, optional): Specifies if the runner should be locked for the current project. Default is False.
        run_untagged (bool, optional): Specifies if the runner should handle untagged jobs. Default is True.
        tag_list (list, optional): A list of runner tags.
        access_level (str, optional): The access level of the runner; 'not_protected' or 'ref_protected'.
        maximum_timeout (int, optional): Maximum timeout that limits the amount of time (in seconds) that runners can run jobs.
        maintenance_note (str, optional): Free-form maintenance notes for the runner (1024 characters).
    
    Returns:
        requests.Response: The API response containing runner information
        
    Example:
        >>> create_user_runner(runner_type='project_type', project_id=183, 
                              description='Test runner for API testing', 
                              tag_list=['test', 'api'])
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/user/runners"
    
    payload = {
        'runner_type': runner_type
    }
    
    if group_id is not None:
        payload['group_id'] = group_id
    
    if project_id is not None:
        payload['project_id'] = project_id
    
    if description is not None:
        payload['description'] = description
    
    if paused is not None:
        payload['paused'] = paused
    
    if locked is not None:
        payload['locked'] = locked
    
    if run_untagged is not None:
        payload['run_untagged'] = run_untagged
    
    if tag_list is not None:
        payload['tag_list'] = tag_list
    
    if access_level is not None:
        payload['access_level'] = access_level
    
    if maximum_timeout is not None:
        payload['maximum_timeout'] = maximum_timeout
    
    if maintenance_note is not None:
        payload['maintenance_note'] = maintenance_note
    
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = create_user_runner(runner_type='project_type', project_id=183, description='Test runner for API testing', tag_list=['test', 'api'])
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