import requests, json
from urllib.parse import quote

def cancel_merge_when_pipeline_succeeds(project_id: str | int, merge_request_iid: int):
    """
    Cancels the automatic merge of a merge request that was previously set to merge when its pipeline succeeds, returning the updated merge request details.
    
    Args:
        project_id (str|int): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        
    Returns:
        requests.Response: The API response containing the updated merge request details.
        
    Example:
        >>> response = cancel_merge_when_pipeline_succeeds(project_id=183, merge_request_iid=1)
        >>> print(response.status_code)
        201
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/cancel_merge_when_pipeline_succeeds"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = cancel_merge_when_pipeline_succeeds(project_id=183, merge_request_iid=1)
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