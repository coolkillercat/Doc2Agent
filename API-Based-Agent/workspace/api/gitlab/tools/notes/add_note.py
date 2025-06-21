import requests, json
from urllib.parse import quote



def add_note(project_id: int, resource_type: str, resource_id: int, body: str, confidential: bool = False) -> dict:
    """
    Creates a new note (comment) on a specific project resource such as issues, merge requests, commits, snippets, or epics. Allows marking comments as confidential.
    
    Args:
        project_id (int): The ID of the project.
        resource_type (str): The type of resource (issue, merge_request, commit, snippet, epic).
        resource_id (int): The ID of the resource.
        body (str): The content of the note.
        confidential (bool, optional): Set to True to create a confidential note. Defaults to False.
    
    Returns:
        Returns information about a newly created note including its content, author details, timestamps, and visibility settings."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Determine the endpoint based on resource type
    if resource_type == "issue":
        url = f"{base_url}/projects/{project_id}/issues/{resource_id}/notes"
    elif resource_type == "merge_request":
        url = f"{base_url}/projects/{project_id}/merge_requests/{resource_id}/notes"
    elif resource_type == "commit":
        url = f"{base_url}/projects/{project_id}/repository/commits/{resource_id}/notes"
    elif resource_type == "snippet":
        url = f"{base_url}/projects/{project_id}/snippets/{resource_id}/notes"
    elif resource_type == "epic":
        url = f"{base_url}/projects/{project_id}/epics/{resource_id}/notes"
    else:
        raise ValueError(f"Invalid resource type: {resource_type}")
    
    data = {
        "body": body,
    }
    
    if confidential:
        data["confidential"] = confidential
    
    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = add_note(project_id=183, resource_type="issue", resource_id=1, body="This is a test comment")
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