import requests, json
from urllib.parse import quote



def get_project_languages(project_id: int) -> dict:
    """
    Retrieves the programming languages used in a GitLab project along with their percentage distribution. Helps developers understand the technology composition of a project.
    
    Args:
        project_id (int): The ID of the GitLab project
        
    Returns:
        Returns the programming languages used in a GitLab project along with their percentage distribution in the codebase."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/projects/{project_id}/languages"
    
    response = requests.get(endpoint, headers=headers)
    return response

if __name__ == '__main__':
    r = get_project_languages(project_id=183)
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