import requests, json
from urllib.parse import quote



def get_issue_discussions(project_id: int, issue_iid: int):
    """
    Retrieves all discussion threads and comments for a specific issue within a project, providing a comprehensive view of the conversation history.
    
    Args:
        project_id (int): The ID of the project containing the issue
        issue_iid (int): The internal ID of the issue
        
    Returns:
        Retrieves all discussion threads and comments for a specific issue within a project, providing a comprehensive view of the conversation history."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/projects/{project_id}/issues/{issue_iid}/discussions"
    
    response = requests.get(endpoint, headers=headers)
    return response

if __name__ == '__main__':
    r = get_issue_discussions(project_id=183, issue_iid=1)
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