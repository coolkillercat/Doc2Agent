import requests, json
from urllib.parse import quote



def remove_project_avatar(project_id: int):
    """
    Removes the avatar image from a GitLab project by setting it to a blank value. Useful for returning projects to their default visual state.
    
    Args:
        project_id (int): The ID of the project from which to remove the avatar
        
    Returns:
        Returns the complete project information with the avatar removed, showing the updated project details with avatar_url set to null."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}"
    
    data = {"avatar": ""}
    
    response = requests.put(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = remove_project_avatar(project_id=183)
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