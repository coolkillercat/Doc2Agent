import requests, json
from urllib.parse import quote

def rebase_merge_request(project_id: str, merge_request_iid: int, skip_ci: bool = False) -> dict:
    """
    Automatically rebases the source branch of a merge request against its target branch.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        skip_ci (bool, optional): Set to True to skip creating a CI pipeline. Defaults to False.
        
    Returns:
        dict: The response from the API as a dictionary.
        
    Example:
        >>> rebase_merge_request(project_id="183", merge_request_iid=20, skip_ci=True)
        {'rebase_in_progress': true}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/rebase"
    
    params = {}
    if skip_ci:
        params['skip_ci'] = 'true'
    
    response = requests.put(url, headers=headers, params=params)
    
    if response.status_code == 202:
        return response.json()
    
    return response

if __name__ == '__main__':
    r = rebase_merge_request(project_id=183, merge_request_iid=1, skip_ci=True)
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