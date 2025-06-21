import requests
from urllib.parse import quote


def get_merge_request_changes(project_id: str, merge_request_iid: int, access_raw_diffs: bool = False, unidiff: bool = False):
    """
    Retrieves detailed information about a merge request including its files and changes.
    
    This endpoint is deprecated in GitLab 15.7 and scheduled for removal in API v5.
    Consider using the List merge request diffs endpoint instead.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        access_raw_diffs (bool, optional): Retrieve change diffs through Gitaly. Defaults to False.
        unidiff (bool, optional): Present change diffs in the unified diff format. Defaults to False.
        
    Returns:
        Response: The HTTP response containing merge request changes information.
        
    Example:
        >>> get_merge_request_changes(project_id="183", merge_request_iid=1)
        >>> get_merge_request_changes(project_id="183", merge_request_iid=1, access_raw_diffs=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    project_id_encoded = quote(str(project_id), safe='')
    
    url = f"{base_url}/projects/{project_id_encoded}/merge_requests/{merge_request_iid}/changes"
    
    params = {}
    if access_raw_diffs:
        params['access_raw_diffs'] = 'true'
    if unidiff:
        params['unidiff'] = 'true'
        
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_merge_request_changes(project_id=183, merge_request_iid=1)
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