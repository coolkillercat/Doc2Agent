import requests, json
from urllib.parse import quote



def start_project_housekeeping(project_id: str, task: str = None):
    """
    Initiates a housekeeping task for a GitLab project to optimize repository storage. Can trigger either manual pruning of unreachable objects or eager housekeeping to improve repository performance.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        task (str, optional): The type of housekeeping task to perform. 
                             'prune' for manual pruning of unreachable objects,
                             'eager' for eager housekeeping. Default is None.
    
    Returns:
        Returns the API response for initiating a project housekeeping task that optimizes repository storage through pruning or eager housekeeping."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/housekeeping"
    
    payload = {}
    if task:
        payload = {'task': task}
    
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = start_project_housekeeping(project_id='183', task='prune')
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