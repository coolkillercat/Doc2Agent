import requests
from urllib.parse import quote

def reset_merge_request_spent_time(project_id: str, merge_request_iid: int, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token: str = "glpat-qvQ-N6mN_tAddXb2WWdi"):
    """
    Resets the total spent time for a specific merge request to 0 seconds.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of a project's merge request
        base_url (str, optional): The base URL for the GitLab API
        token (str, optional): The private token for authentication
    
    Returns:
        Response: The HTTP response from the API
        
    Example:
        >>> response = reset_merge_request_spent_time(project_id="183", merge_request_iid=1)
        >>> print(response.status_code)
        200
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/reset_spent_time"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = reset_merge_request_spent_time(project_id=183, merge_request_iid=1)
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