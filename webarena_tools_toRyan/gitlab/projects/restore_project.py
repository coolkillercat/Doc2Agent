import requests
from urllib.parse import quote


def restore_project(project_id: str, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", 
                   token: str = "GITLAB_KEY_REMOVED") -> dict:
    """
    Restores a project that has been marked for deletion. This allows recovering projects that are in the deletion queue before they are permanently removed.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project to restore.
        base_url (str, optional): The base URL of the GitLab API.
        token (str, optional): The private token for authentication.
        
    Returns:
        dict: Response object from the API request.
        
    Example:
        >>> restore_project("183")
        <Response [200]>
        
        >>> restore_project("my-group/my-project")
        <Response [200]>
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/restore"
    
    response = requests.post(url, headers=headers)
    return response


if __name__ == '__main__':
    r = restore_project(project_id="183")
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