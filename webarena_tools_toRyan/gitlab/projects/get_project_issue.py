import requests, json
from urllib.parse import quote



def get_project_issue(project_id: str, issue_iid: int):
    """
    Retrieves detailed information about a specific issue within a GitLab project, including its status, assignees, description, time statistics, and other metadata.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the project's issue
        
    Returns:
        Returns detailed information about a specific GitLab project issue, including its status, assignees, description, time statistics, and metadata."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL encode the project_id if it contains slashes or special characters
    encoded_project_id = quote(str(project_id), safe='')
    
    url = f"{base_url}/projects/{encoded_project_id}/issues/{issue_iid}"
    response = requests.get(url, headers=headers)
    
    return response

if __name__ == '__main__':
    r = get_project_issue(project_id="183", issue_iid=1)
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