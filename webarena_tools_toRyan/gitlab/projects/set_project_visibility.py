import requests, json
from urllib.parse import quote



def set_project_visibility(project_id: int, visibility: str):
    """
    Updates the visibility level of a GitLab project. The visibility parameter can be 'private', 'internal', or 'public' to control who can access the project.
    
    Args:
        project_id (int): The ID of the project to update
        visibility (str): The visibility level to set. Must be one of 'private', 'internal', or 'public'
    
    Returns:
        Returns the complete project details including metadata, settings, permissions, and visibility level after updating the project's visibility."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Ensure visibility is one of the allowed values
    if visibility not in ['private', 'internal', 'public']:
        raise ValueError("Visibility must be one of 'private', 'internal', or 'public'")
    
    # Construct the URL
    url = f"{base_url}/projects/{project_id}"
    
    # Prepare data for the request
    data = {
        'visibility': visibility
    }
    
    # Make the PUT request to update project visibility
    response = requests.put(url, headers=headers, json=data)
    
    return response

if __name__ == '__main__':
    r = set_project_visibility(project_id=183, visibility='public')
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