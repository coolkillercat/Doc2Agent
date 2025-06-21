import requests, json
from urllib.parse import quote

def get_merge_request_state_events(project_id: str, merge_request_iid: int):
    """
    Retrieves the history of state changes for a specific merge request, including who changed the state and when it occurred.
    This is useful for tracking the progression of a merge request through different states (e.g., opened, closed, merged).
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of the merge request
        
    Returns:
        requests.Response: The API response containing merge request state events
        
    Example:
        >>> response = get_merge_request_state_events(project_id='183', merge_request_iid=1)
        >>> print(response.status_code)
        200
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/resource_state_events"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_merge_request_state_events(project_id='183', merge_request_iid=1)
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