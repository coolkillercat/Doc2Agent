import requests, json
from urllib.parse import quote

def list_merge_request_pipelines(project_id, merge_request_iid, page=1, per_page=20):
    """
    Retrieves a list of pipelines associated with a specific merge request in a project, allowing developers to track CI/CD processes for code changes.
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of the merge request
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of items per page. Defaults to 20.
        
    Returns:
        Response: The HTTP response from the API
        
    Example:
        >>> list_merge_request_pipelines(183, 1)
        >>> list_merge_request_pipelines("group/project", 20, page=2, per_page=10)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL encode the project_id if it's a path
    if not str(project_id).isdigit():
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/merge_requests/{merge_request_iid}/pipelines"
    params = {
        'page': page,
        'per_page': per_page
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_merge_request_pipelines(project_id=183, merge_request_iid=1)
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