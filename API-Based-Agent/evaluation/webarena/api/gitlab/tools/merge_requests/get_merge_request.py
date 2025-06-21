import requests, json
from urllib.parse import quote


def get_merge_request(project_id: int, merge_request_iid: int, include_diverged_commits_count: bool = False, 
                     include_rebase_in_progress: bool = False, render_html: bool = False, 
                     with_merge_status_recheck: bool = False):
    """
    Retrieves detailed information about a specific merge request in a project, including its current status, assignees, and other metadata.
    
    Args:
        project_id (int): The ID of the project
        merge_request_iid (int): The internal ID of the merge request
        include_diverged_commits_count (bool, optional): Whether to include the commits count that would be removed by a rebase. Defaults to False.
        include_rebase_in_progress (bool, optional): Whether to include if a rebase operation is in progress. Defaults to False.
        render_html (bool, optional): Whether to render HTML in the description. Defaults to False.
        with_merge_status_recheck (bool, optional): Whether to check if the merge status is up to date. Defaults to False.
        
    Returns:
        dict: The JSON response containing merge request information
        
    Example:
        >>> get_merge_request(project_id=183, merge_request_iid=1)
        {
            "id": 1,
            "iid": 1,
            "project_id": 183,
            "title": "Example merge request",
            ...
        }
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/merge_requests/{merge_request_iid}"
    
    params = {}
    if include_diverged_commits_count:
        params['include_diverged_commits_count'] = include_diverged_commits_count
    if include_rebase_in_progress:
        params['include_rebase_in_progress'] = include_rebase_in_progress
    if render_html:
        params['render_html'] = render_html
    if with_merge_status_recheck:
        params['with_merge_status_recheck'] = with_merge_status_recheck
    
    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else response

if __name__ == '__main__':
    r = get_merge_request(project_id=183, merge_request_iid=1)
    r_json = None
    try:
        r_json = r if isinstance(r, dict) else r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code if hasattr(r, 'status_code') else None
    result_dict['text'] = r.text if hasattr(r, 'text') else json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8") if hasattr(r, 'content') else json.dumps(r)
    print(json.dumps(result_dict, indent=4))