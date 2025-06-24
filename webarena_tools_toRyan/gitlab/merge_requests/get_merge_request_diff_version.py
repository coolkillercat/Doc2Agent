import requests, json
from urllib.parse import quote


def get_merge_request_diff_version(project_id: str, merge_request_iid: int, version_id: int, unidiff: bool = False):
    """
    Retrieves a specific version of a merge request diff, including commit details and file changes.
    
    This function fetches a single merge request diff version with all its details including commits,
    file changes, and metadata. Useful for code review workflows and tracking how a merge request 
    has evolved over time.
    
    Args:
        project_id (str): ID of the project (e.g., "183")
        merge_request_iid (int): Internal ID of the merge request (e.g., 1)
        version_id (int): ID of the merge request diff version (e.g., 1)
        unidiff (bool, optional): Whether to present diffs in unified diff format. Defaults to False.
    
    Returns:
        requests.Response: The API response containing the merge request diff version data
        
    Example:
        >>> response = get_merge_request_diff_version("183", 1, 1)
        >>> response = get_merge_request_diff_version("183", 1, 1, unidiff=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id))}/merge_requests/{merge_request_iid}/versions/{version_id}"
    
    params = {}
    if unidiff:
        params['unidiff'] = True
    
    response = requests.get(url, headers=headers, params=params)
    return response


if __name__ == '__main__':
    r = get_merge_request_diff_version(project_id="183", merge_request_iid=1, version_id=1)
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