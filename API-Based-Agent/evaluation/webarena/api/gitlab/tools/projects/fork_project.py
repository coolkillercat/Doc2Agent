import requests, json
from urllib.parse import quote

def fork_project(project_id: str, branches: str = None, description: str = None, mr_default_target_self: bool = None, name: str = None, namespace_id: int = None, namespace_path: str = None, path: str = None, visibility: str = None):
    """
    Creates a fork of an existing project in the user's namespace or a specified namespace. The fork operation runs asynchronously in the background and returns immediately.
    
    Parameters:
        project_id (str): The ID or URL-encoded path of the project to fork.
        branches (str, optional): Branches to fork (empty for all branches).
        description (str, optional): The description assigned to the resultant project after forking.
        mr_default_target_self (bool, optional): For forked projects, target merge requests to this project. If False, the target is the upstream project.
        name (str, optional): The name assigned to the resultant project after forking.
        namespace_id (int, optional): The ID of the namespace that the project is forked to.
        namespace_path (str, optional): The path of the namespace that the project is forked to.
        path (str, optional): The path assigned to the resultant project after forking.
        visibility (str, optional): The visibility level assigned to the resultant project after forking.
    
    Returns:
        requests.Response: The response from the API call.
        
    Example:
        >>> fork_project(project_id="183", namespace_path="byteblaze", name="forked_project", description="Fork of the original project")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/fork"
    
    data = {}
    if branches is not None:
        data['branches'] = branches
    if description is not None:
        data['description'] = description
    if mr_default_target_self is not None:
        data['mr_default_target_self'] = mr_default_target_self
    if name is not None:
        data['name'] = name
    if namespace_id is not None:
        data['namespace_id'] = namespace_id
    if namespace_path is not None:
        data['namespace_path'] = namespace_path
    if path is not None:
        data['path'] = path
    if visibility is not None:
        data['visibility'] = visibility
    
    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = fork_project(project_id=183, namespace_path="byteblaze", name="forked_project", description="Fork of the original project")
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