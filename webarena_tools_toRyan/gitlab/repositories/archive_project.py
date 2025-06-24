import requests, json
from urllib.parse import quote


def archive_project(project_id: int or str) -> dict:
    """
    Archives a GitLab project. This function allows administrators or project owners to archive a project, making it read-only. Returns the full project details with archived status.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project to archive
        
    Returns:
        Returns the complete details of a GitLab project after archiving it, including its metadata, permissions, settings, and archived status.
    Example:
        >>> archive_project(183)
        {'id': 183, 'description': '...', 'archived': true, ...}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/archive"
    
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    
    return response.json()

if __name__ == '__main__':
    r = archive_project(project_id=183)
    r_json = None
    try:
        r_json = r
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))