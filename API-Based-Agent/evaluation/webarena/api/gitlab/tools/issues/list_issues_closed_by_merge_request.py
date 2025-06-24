import requests
from urllib.parse import quote

def list_issues_closed_by_merge_request(project_id, merge_request_iid):
    """
    Retrieves all issues that would be automatically closed if the specified merge request were merged.
    Useful for reviewing the impact of a merge request before approval.
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        
    Returns:
        requests.Response: The API response containing issues that would be closed by the merge request.
        
    Example:
        >>> response = list_issues_closed_by_merge_request(183, 1)
        >>> issues = response.json()
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/closes_issues"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = list_issues_closed_by_merge_request(project_id=183, merge_request_iid=1)
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