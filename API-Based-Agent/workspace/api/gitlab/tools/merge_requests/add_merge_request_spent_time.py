import requests, json
from urllib.parse import quote

def add_merge_request_spent_time(project_id, merge_request_iid, duration, summary=None):
    """
    Records time spent working on a specific merge request. The duration is specified in human-readable format (e.g., '3h30m') and an optional summary can be provided to describe how the time was spent.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        duration (str): The duration in human format, such as '3h30m'.
        summary (str, optional): A summary of how the time was spent.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> add_merge_request_spent_time(183, 1, '1h30m', 'Code review and testing')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id))}/merge_requests/{merge_request_iid}/add_spent_time"
    
    params = {'duration': duration}
    if summary:
        params['summary'] = summary
    
    response = requests.post(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = add_merge_request_spent_time(project_id=183, merge_request_iid=1, duration='1h30m', summary='Code review and testing')
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