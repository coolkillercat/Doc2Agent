import requests, json
from urllib.parse import quote



def get_merge_requests_related_to_issue(project_id: str, issue_iid: int):
    """
    Retrieves all merge requests that are related to a specific issue in a project, showing their details such as state, author, milestone, and pipeline information.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the project issue
        
    Returns:
        Returns all merge requests related to a specific issue in a project, including their state, author, milestone, and pipeline information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"/projects/{quote(str(project_id))}/issues/{issue_iid}/related_merge_requests"
    
    url = base_url + endpoint
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_merge_requests_related_to_issue(project_id=183, issue_iid=1)
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