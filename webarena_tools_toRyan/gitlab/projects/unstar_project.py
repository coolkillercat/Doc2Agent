import requests, json
from urllib.parse import quote


def unstar_project(project_id: str) -> dict:
    """
    Removes a star from a GitLab project. This function allows users to unstar a project they previously starred, decreasing its star count. Returns the updated project details.
    
    Args:
        project_id (str): The ID of the project to unstar
        
    Returns:
        Returns the updated project details after removing a star from a GitLab project, including its ID, name, and current star count.
    Example:
        >>> unstar_project('183')
        {
            "id": 183,
            "name": "Project Name",
            "star_count": 0,
            ...
        }
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/unstar"
    response = requests.post(url, headers=headers)
    
    result = {
        'status_code': response.status_code,
        'text': response.text,
        'content': response.content.decode("utf-8")
    }
    
    try:
        result['json'] = response.json()
    except json.JSONDecodeError:
        result['json'] = None
    
    return result


if __name__ == '__main__':
    r = unstar_project(project_id='183')
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r['status_code']
    result_dict['text'] = r['text']
    result_dict['json'] = r_json
    result_dict['content'] = r['content']
    print(json.dumps(result_dict, indent=4))