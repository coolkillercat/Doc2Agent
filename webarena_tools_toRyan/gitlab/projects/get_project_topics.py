import requests
from urllib.parse import quote

def get_project_topics(project_id: int, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token: str = "GITLAB_KEY_REMOVED") -> list:
    """
    Retrieve the topics associated with a GitLab project, providing a modern alternative to the deprecated tag_list attribute. 
    Topics help categorize projects for better organization and discoverability.
    
    Args:
        project_id (int): The ID of the project to retrieve topics for.
        base_url (str, optional): The base URL of the GitLab API.
        token (str, optional): The private token for authentication.
        
    Returns:
        list: A list of project topics.
        
    Example:
        >>> get_project_topics(183)
        ['api', 'test']
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/projects/{project_id}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        project_data = response.json()
        return project_data.get('topics', [])
    
    return []

if __name__ == '__main__':
    r = get_project_topics(project_id=183)
    r_json = None
    try:
        r_json = r
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200 if r else 404
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))