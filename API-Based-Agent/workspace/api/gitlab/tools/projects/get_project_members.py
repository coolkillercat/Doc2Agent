import requests, json
from urllib.parse import quote



def get_project_members(project_id: str) -> list:
    """
    Retrieves a list of all members associated with a specific project. This helps project managers understand team composition and permissions.
    
    Args:
        project_id (str): The ID of the project to get members from
        
    Returns:
        Returns a list of all members associated with a specific project, including their user details, access levels, and creation information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/projects/{project_id}/members"
    
    response = requests.get(endpoint, headers=headers)
    return response

if __name__ == '__main__':
    r = get_project_members(project_id="183")  # Added project_id parameter
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