import requests, json
from urllib.parse import quote


def subscribe_to_merge_request(project_id: str, merge_request_iid: int) -> dict:
    """
    Subscribes the authenticated user to a specific merge request to receive notifications about updates and changes.
    Returns the detailed merge request information.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of the merge request
        
    Returns:
        dict: The merge request information after subscription
        
    Example:
        >>> subscribe_to_merge_request(project_id='183', merge_request_iid=1)
        {'id': 1, 'iid': 1, 'project_id': 183, ...}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id))}/merge_requests/{merge_request_iid}/subscribe"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = subscribe_to_merge_request(project_id=183, merge_request_iid=1)
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