import requests, json
from urllib.parse import quote

def get_group_issues(group_id: str, state: str = None, labels: str = None, milestone: str = None, assignee_id: int = None, 
                     author_id: int = None, search: str = None, confidential: bool = None, created_after: str = None, 
                     created_before: str = None, due_date: str = None, sort: str = 'desc', order_by: str = 'created_at', 
                     issue_type: str = None, scope: str = None, weight: int = None, assignee_username: str = None,
                     author_username: str = None, epic_id: int = None, iids: list = None, iteration_id: int = None,
                     iteration_title: str = None, my_reaction_emoji: str = None, non_archived: bool = None,
                     updated_after: str = None, updated_before: str = None, with_labels_details: bool = None):
    """
    Retrieves issues from a specific group with flexible filtering options.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group.
        state (str, optional): Return all issues or just those that are 'opened' or 'closed'.
        labels (str, optional): Comma-separated list of label names, issues must have all labels to be returned.
        milestone (str, optional): The milestone title. 'None' lists all issues with no milestone. 'Any' lists all issues that have an assigned milestone.
        assignee_id (int, optional): Return issues assigned to the given user ID.
        assignee_username (str, optional): Return issues assigned to the given username.
        author_id (int, optional): Return issues created by the given user ID.
        author_username (str, optional): Return issues created by the given username.
        search (str, optional): Search group issues against their title and description.
        confidential (bool, optional): Filter confidential or public issues.
        created_after (str, optional): Return issues created on or after the given time (ISO 8601 format).
        created_before (str, optional): Return issues created on or before the given time (ISO 8601 format).
        due_date (str, optional): Return issues based on due date criteria.
        sort (str, optional): Return issues sorted in 'asc' or 'desc' order. Default is 'desc'.
        order_by (str, optional): Return issues ordered by specified field. Default is 'created_at'.
        issue_type (str, optional): Filter to a given type of issue. One of 'issue', 'incident', 'test_case' or 'task'.
        scope (str, optional): Return issues for the given scope: 'created_by_me', 'assigned_to_me' or 'all'. Default is 'all'.
        weight (int, optional): Return issues with the specified weight.
        epic_id (int, optional): Return issues associated with the given epic ID.
        iids (list, optional): Return only the issues having the given iids.
        iteration_id (int, optional): Return issues assigned to the given iteration ID.
        iteration_title (str, optional): Return issues assigned to the iteration with the given title.
        my_reaction_emoji (str, optional): Return issues reacted by the authenticated user by the given emoji.
        non_archived (bool, optional): Return issues from non archived projects. Default is true.
        updated_after (str, optional): Return issues updated on or after the given time (ISO 8601 format).
        updated_before (str, optional): Return issues updated on or before the given time (ISO 8601 format).
        with_labels_details (bool, optional): If true, the response returns more details for each label.
        
    Returns:
        requests.Response: The API response containing the group issues.
        
    Example:
        >>> get_group_issues(group_id='183', state='opened', labels='bug,urgent')
        >>> get_group_issues(group_id='183', assignee_id=2330, created_after='2023-01-01T00:00:00Z')
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # URL encode the group_id if it's a path
    encoded_group_id = quote(str(group_id), safe='')
    
    url = f"{base_url}/groups/{encoded_group_id}/issues"
    
    params = {}
    
    # Add all the optional parameters if they are provided
    if state is not None:
        params['state'] = state
    if labels is not None:
        params['labels'] = labels
    if milestone is not None:
        params['milestone'] = milestone
    if assignee_id is not None:
        params['assignee_id'] = assignee_id
    if assignee_username is not None:
        params['assignee_username'] = assignee_username
    if author_id is not None:
        params['author_id'] = author_id
    if author_username is not None:
        params['author_username'] = author_username
    if search is not None:
        params['search'] = search
    if confidential is not None:
        params['confidential'] = confidential
    if created_after is not None:
        params['created_after'] = created_after
    if created_before is not None:
        params['created_before'] = created_before
    if due_date is not None:
        params['due_date'] = due_date
    if sort is not None:
        params['sort'] = sort
    if order_by is not None:
        params['order_by'] = order_by
    if issue_type is not None:
        params['issue_type'] = issue_type
    if scope is not None:
        params['scope'] = scope
    if weight is not None:
        params['weight'] = weight
    if epic_id is not None:
        params['epic_id'] = epic_id
    if iids is not None:
        params['iids[]'] = iids
    if iteration_id is not None:
        params['iteration_id'] = iteration_id
    if iteration_title is not None:
        params['iteration_title'] = iteration_title
    if my_reaction_emoji is not None:
        params['my_reaction_emoji'] = my_reaction_emoji
    if non_archived is not None:
        params['non_archived'] = non_archived
    if updated_after is not None:
        params['updated_after'] = updated_after
    if updated_before is not None:
        params['updated_before'] = updated_before
    if with_labels_details is not None:
        params['with_labels_details'] = with_labels_details
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_group_issues(group_id='183', state='opened', labels='bug,urgent', sort='asc', order_by='updated_at')
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