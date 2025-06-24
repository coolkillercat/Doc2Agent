import requests, json
from urllib.parse import quote

def get_project_issues(project_id: int, state: str = 'opened', labels: list = None, milestone: str = None, search: str = None, sort: str = 'created_at', order_by: str = 'desc', created_after: str = None, created_before: str = None, updated_after: str = None, updated_before: str = None, assignee_id: int = None, author_id: int = None, confidential: bool = None, per_page: int = 20, page: int = 1):
    """
    Retrieves issues from a GitLab project with flexible filtering options. Allows users to search, filter, and sort issues based on various criteria like state, labels, milestone, creation date, and assignees.
    
    Args:
        project_id (int): The ID of the project.
        state (str, optional): Return all issues or just those that are opened or closed. Defaults to 'opened'.
        labels (list, optional): A list of label names. Defaults to None.
        milestone (str, optional): The milestone title. Defaults to None.
        search (str, optional): Search issues for the given string. Defaults to None.
        sort (str, optional): Sort issues by created_at, updated_at, or other fields. Defaults to 'created_at'.
        order_by (str, optional): Order issues by asc or desc. Defaults to 'desc'.
        created_after (str, optional): Return issues created after the given time. Defaults to None.
        created_before (str, optional): Return issues created before the given time. Defaults to None.
        updated_after (str, optional): Return issues updated after the given time. Defaults to None.
        updated_before (str, optional): Return issues updated before the given time. Defaults to None.
        assignee_id (int, optional): Return issues assigned to the given user ID. Defaults to None.
        author_id (int, optional): Return issues created by the given user ID. Defaults to None.
        confidential (bool, optional): Filter confidential or public issues. Defaults to None.
        per_page (int, optional): Number of items to list per page. Defaults to 20.
        page (int, optional): Page number of the results to fetch. Defaults to 1.
        
    Returns:
        Response: The response object from the API request.
        
    Example:
        >>> get_project_issues(project_id=183, state='all', labels=['bug', 'feature'], author_id=2330)
        <Response [200]>
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Build base URL
    base_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{project_id}/issues"
    
    # Prepare query parameters
    params = {
        'state': state,
        'sort': sort,
        'order_by': order_by,
        'per_page': per_page,
        'page': page
    }
    
    # Add optional parameters if provided
    if labels:
        params['labels'] = ','.join(labels)
    if milestone:
        params['milestone'] = milestone
    if search:
        params['search'] = search
    if created_after:
        params['created_after'] = created_after
    if created_before:
        params['created_before'] = created_before
    if updated_after:
        params['updated_after'] = updated_after
    if updated_before:
        params['updated_before'] = updated_before
    if assignee_id is not None:
        params['assignee_id'] = assignee_id
    if author_id is not None:
        params['author_id'] = author_id
    if confidential is not None:
        params['confidential'] = confidential
    
    # Make the API request
    response = requests.get(base_url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_project_issues(project_id=183, state='all', labels=['bug', 'feature'], author_id=2330, per_page=10)
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