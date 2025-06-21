import requests, json
from urllib.parse import quote

def get_merge_request_reviewers(project_id, merge_request_iid, base_url="http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"):
    """
    Retrieves a list of reviewers assigned to a specific merge request, including their user information and review state (unreviewed/reviewed).
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project
        merge_request_iid (int): The internal ID of the merge request
        base_url (str, optional): The base URL for the GitLab API
        
    Returns:
        requests.Response: The response object containing the list of reviewers
        
    Example:
        >>> response = get_merge_request_reviewers(183, 1)
        >>> reviewers = response.json()
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Encode the project_id to handle special characters
    encoded_project_id = quote(str(project_id), safe='')
    
    # Construct the URL
    url = f"{base_url}/projects/{encoded_project_id}/merge_requests/{merge_request_iid}/reviewers"
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    return response

if __name__ == '__main__':
    r = get_merge_request_reviewers(project_id=183, merge_request_iid=1)
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