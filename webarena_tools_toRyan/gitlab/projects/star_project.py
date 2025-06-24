import requests, json
from urllib.parse import quote



def star_project(project_id: int or str) -> dict:
    """
    Stars a GitLab project for the authenticated user, making it easier to find in their starred projects list. Returns the complete project details after starring.
    
    Args:
        project_id: The ID or URL-encoded path of the project to star
        
    Returns:
        Returns the complete details of a GitLab project after starring it for the authenticated user."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Handle both integer and string project IDs
    if isinstance(project_id, str):
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/star"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = star_project(project_id=183)
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