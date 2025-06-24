import requests, json
from urllib.parse import quote



def get_project_starrers(project_id: int, search: str = None):
    """
    Retrieves a list of users who have starred a specific GitLab project. Optionally filter results by searching for specific users.
    
    Args:
        project_id (int): The ID of the project to get starrers for
        search (str, optional): Search term to filter users by. Defaults to None.
    
    Returns:
        Returns a list of users who have starred a specific GitLab project, including when they starred it and their user details."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/starrers"
    
    params = {}
    if search:
        params['search'] = search
        
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_starrers(project_id=183)
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