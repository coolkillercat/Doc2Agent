import requests
from urllib.parse import quote

def get_merge_request_approvals(project_id, merge_request_iid, base_url=None, headers=None):
    """
    Retrieves approval information for a specific merge request, allowing users to see who has approved the merge request and what approval rules apply.
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of the merge request
        base_url (str, optional): The base URL for the GitLab API
        headers (dict, optional): Headers to include in the request
        
    Returns:
        requests.Response: The API response containing approval information for the merge request
        
    Example:
        >>> response = get_merge_request_approvals(project_id=183, merge_request_iid=1)
        >>> response = get_merge_request_approvals("my-group/my-project", 20)
    """
    if headers is None:
        headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    if base_url is None:
        base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/approvals"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_merge_request_approvals(project_id="183", merge_request_iid=1)
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