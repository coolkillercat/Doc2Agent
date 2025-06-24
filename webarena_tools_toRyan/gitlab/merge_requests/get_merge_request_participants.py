import requests, json
from urllib.parse import quote

def get_merge_request_participants(project_id, merge_request_iid):
    """
    Retrieves a list of all participants involved in a specific merge request, providing user details such as name, username, avatar URL, and web URL. This helps project managers and team members identify who has contributed to or reviewed a particular merge request.
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project owned by the authenticated user
        merge_request_iid (int): The internal ID of the merge request
        
    Returns:
        requests.Response: The API response containing the list of merge request participants
        
    Example:
        >>> response = get_merge_request_participants(project_id=183, merge_request_iid=1)
        >>> participants = response.json()
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL encode the project_id to handle special characters
    encoded_project_id = quote(str(project_id), safe='')
    
    url = f"{base_url}/projects/{encoded_project_id}/merge_requests/{merge_request_iid}/participants"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_merge_request_participants(project_id=183, merge_request_iid=1)
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