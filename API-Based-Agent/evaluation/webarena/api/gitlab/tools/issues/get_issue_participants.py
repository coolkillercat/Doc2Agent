import requests, json
from urllib.parse import quote



def get_issue_participants(project_id: str, issue_iid: int):
    """
    Retrieves a list of users who are participants in a specific GitLab project issue. This helps project managers and team members identify who is involved in discussions or assigned to a particular issue.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the project's issue
        
    Returns:
        Returns a list of users who are participants in a specific GitLab project issue, including their profile information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL-encode the project ID if it's a path
    if not str(project_id).isdigit():
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/issues/{issue_iid}/participants"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_issue_participants(project_id=183, issue_iid=1)
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