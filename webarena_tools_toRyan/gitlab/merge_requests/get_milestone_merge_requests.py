import requests
from urllib.parse import quote

def get_milestone_merge_requests(project_id, milestone_id, state=None, order_by=None, sort='desc'):
    """
    Retrieves all merge requests assigned to a specific project milestone. Allows filtering by state and customizing the order of results.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project owned by the authenticated user
        milestone_id (int): The ID of the project's milestone
        state (str, optional): Filter merge requests by state (opened, closed, merged, all)
        order_by (str, optional): Return merge requests ordered by created_at, updated_at, or title fields
        sort (str, optional): Return merge requests sorted in asc or desc order (default: 'desc')
        
    Returns:
        requests.Response: The API response containing merge requests assigned to the milestone
        
    Example:
        >>> get_milestone_merge_requests(183, 1)
        >>> get_milestone_merge_requests(183, 1, state='opened', order_by='created_at', sort='asc')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # Construct the base URL
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_project_id = quote(str(project_id), safe='')
    url = f"{base_url}/projects/{encoded_project_id}/milestones/{milestone_id}/merge_requests"
    
    # Build query parameters
    params = {}
    if state:
        params['state'] = state
    if order_by:
        params['order_by'] = order_by
    if sort:
        params['sort'] = sort
    
    # Make the API request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_milestone_merge_requests(project_id=183, milestone_id=1)
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