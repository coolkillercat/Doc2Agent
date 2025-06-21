import requests, json
from urllib.parse import quote



def create_todo_for_issue(project_id: str, issue_iid: int):
    """
    Creates a to-do item for the current user on a specific issue, helping users track issues they need to address or follow up on.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        issue_iid (int): The internal ID of the project's issue.
        
    Returns:
        Returns a to-do item with details about the issue, project, author, and tracking information for the current user."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/issues/{issue_iid}/todo"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = create_todo_for_issue(project_id=183, issue_iid=1)
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