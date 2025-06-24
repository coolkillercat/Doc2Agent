import requests, json
from urllib.parse import quote

def get_merge_request_diffs(project_id: str, merge_request_iid: int, page: int = 1, per_page: int = 20, unidiff: bool = False):
    """
    Retrieves the list of file diffs in a merge request, showing what changes were made to each file including additions, deletions, and modifications.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        page (int, optional): The page of results to return. Defaults to 1.
        per_page (int, optional): The number of results per page. Defaults to 20.
        unidiff (bool, optional): Present diffs in the unified diff format. Defaults to False.
    
    Returns:
        Response: The HTTP response object containing the list of diffs.
        
    Example:
        >>> get_merge_request_diffs(project_id='183', merge_request_iid=1)
        >>> get_merge_request_diffs(project_id='183', merge_request_iid=1, page=2, per_page=10, unidiff=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_project_id = quote(str(project_id), safe='')
    
    url = f"{base_url}/projects/{encoded_project_id}/merge_requests/{merge_request_iid}/diffs"
    
    params = {
        'page': page,
        'per_page': per_page
    }
    
    if unidiff:
        params['unidiff'] = True
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_merge_request_diffs(project_id='183', merge_request_iid=1, page=1, per_page=20)
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