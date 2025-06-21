import requests, json
from urllib.parse import quote



def list_issues(scope: str = 'created_by_me', state: str = None, assignee_id: int = None, assignee_username: str = None, author_id: int = None, author_username: str = None, labels: str = None, milestone: str = None, search: str = None, confidential: bool = None, created_after: str = None, created_before: str = None, updated_after: str = None, updated_before: str = None, due_date: str = None, issue_type: str = None, order_by: str = 'created_at', sort: str = 'desc', with_labels_details: bool = False):
    """
    Retrieves issues from GitLab with powerful filtering options. Allows querying by assignee, author, labels, milestone, date ranges and other attributes to help teams track and manage their issues efficiently.
    
    Args:
        scope (str): Return issues for the given scope: 'created_by_me', 'assigned_to_me' or 'all'. Default is 'created_by_me'.
        state (str): Return 'all' issues or just those that are 'opened' or 'closed'.
        assignee_id (int): Return issues assigned to the given user ID.
        assignee_username (str): Return issues assigned to the given username.
        author_id (int): Return issues created by the given user ID.
        author_username (str): Return issues created by the given username.
        labels (str): Comma-separated list of label names.
        milestone (str): The milestone title.
        search (str): Search issues against their title and description.
        confidential (bool): Filter confidential or public issues.
        created_after (str): Return issues created on or after the given time (ISO 8601 format).
        created_before (str): Return issues created on or before the given time (ISO 8601 format).
        updated_after (str): Return issues updated on or after the given time (ISO 8601 format).
        updated_before (str): Return issues updated on or before the given time (ISO 8601 format).
        due_date (str): Return issues with specified due date status.
        issue_type (str): Filter to a given type of issue (issue, incident, test_case, task).
        order_by (str): Return issues ordered by specified field. Default is 'created_at'.
        sort (str): Return issues sorted in 'asc' or 'desc' order. Default is 'desc'.
        with_labels_details (bool): If True, return more details for each label. Default is False.
    
    Returns:
        Returns a list of GitLab issues with detailed metadata including title, description, state, assignees, labels, and time tracking information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = "/issues"
    
    params = {}
    
    # Add parameters to the request if they are provided
    if scope:
        params['scope'] = scope
    if state:
        params['state'] = state
    if assignee_id:
        params['assignee_id'] = assignee_id
    if assignee_username:
        params['assignee_username'] = assignee_username
    if author_id:
        params['author_id'] = author_id
    if author_username:
        params['author_username'] = author_username
    if labels:
        params['labels'] = labels
    if milestone:
        params['milestone'] = milestone
    if search:
        params['search'] = search
    if confidential is not None:
        params['confidential'] = confidential
    if created_after:
        params['created_after'] = created_after
    if created_before:
        params['created_before'] = created_before
    if updated_after:
        params['updated_after'] = updated_after
    if updated_before:
        params['updated_before'] = updated_before
    if due_date:
        params['due_date'] = due_date
    if issue_type:
        params['issue_type'] = issue_type
    if order_by:
        params['order_by'] = order_by
    if sort:
        params['sort'] = sort
    if with_labels_details:
        params['with_labels_details'] = with_labels_details
    
    url = f"{base_url}{endpoint}"
    
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = list_issues(scope='all', author_id=2330, state='opened')
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