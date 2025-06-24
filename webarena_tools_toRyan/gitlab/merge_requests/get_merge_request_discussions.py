import requests
from urllib.parse import quote

def get_merge_request_discussions(project_id, merge_request_iid):
    """
    Retrieves all discussion threads and comments for a specific merge request, allowing users to review feedback and commentary on code changes.
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project.
        merge_request_iid (int): The IID of the merge request.
        
    Returns:
        dict: The API response containing all discussion threads for the merge request.
        
    Example:
        >>> get_merge_request_discussions(183, 1)
        [
            {
                "id": "6a9c1750b37d513a43987b574953fceb50b03ce7",
                "individual_note": false,
                "notes": [...]
            },
            ...
        ]
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # URL encode the project_id if it's a path
    if isinstance(project_id, str) and '/' in project_id:
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/merge_requests/{merge_request_iid}/discussions"
    
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response

if __name__ == '__main__':
    r = get_merge_request_discussions(project_id=183, merge_request_iid=1)
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