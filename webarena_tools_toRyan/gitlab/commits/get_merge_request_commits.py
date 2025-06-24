import requests, json
from urllib.parse import quote

def get_merge_request_commits(project_id: str, merge_request_iid: int):
    """
    Retrieves a list of commits for a specific merge request, allowing developers to analyze changes, 
    review commit history, and track code contributions within the merge request.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of the merge request
        
    Returns:
        Response object containing the API response with merge request commits
        
    Example:
        >>> get_merge_request_commits(project_id='183', merge_request_iid=1)
        <Response [200]>
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    url = f"{base_url}/projects/{quote(str(project_id))}/merge_requests/{merge_request_iid}/commits"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_merge_request_commits(project_id=183, merge_request_iid=1)
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