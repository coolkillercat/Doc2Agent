import requests, json
from urllib.parse import quote



def import_project_members(target_project_id: str, source_project_id: str):
    """
    Imports members from a source project to a target project, preserving appropriate role hierarchies. 
    Useful for team consolidation or when setting up new projects with existing team structures.
    
    Args:
        target_project_id (str): The ID of the target project to receive the members
        source_project_id (str): The ID of the source project to import the members from
        
    Returns:
        Returns the status and message indicating whether members were successfully imported from a source project to a target project."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{target_project_id}/import_project_members/{source_project_id}"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = import_project_members(target_project_id="183", source_project_id="182")
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