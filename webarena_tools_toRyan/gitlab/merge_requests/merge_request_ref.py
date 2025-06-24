import requests, json
from urllib.parse import quote


def merge_request_ref(project_id: str, merge_request_iid: int):
    """
    Merges changes between source and target branches into a special reference path (refs/merge-requests/:iid/merge) 
    without affecting the actual target branch, allowing preview of the merge result.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of the merge request
        
    Returns:
        requests.Response: The API response containing the commit ID of the merge reference
        
    Example:
        >>> response = merge_request_ref(project_id="183", merge_request_iid=1)
        >>> print(response.status_code)
        200
        >>> print(response.json())
        {'commit_id': '854a3a7a17acbcc0bbbea170986df1eb60435f34'}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id))}/merge_requests/{merge_request_iid}/merge_ref"
    
    response = requests.get(url, headers=headers)
    return response


if __name__ == '__main__':
    r = merge_request_ref(project_id=183, merge_request_iid=1)
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