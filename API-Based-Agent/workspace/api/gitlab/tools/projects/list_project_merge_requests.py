import requests, json
from urllib.parse import quote



def list_project_merge_requests(project_id: str, state: str = None, labels: str = None, milestone: str = None, scope: str = None, author_username: str = None, assignee_id: int = None, reviewer_username: str = None, created_after: str = None, created_before: str = None, source_branch: str = None, target_branch: str = None, search: str = None, sort: str = 'desc', order_by: str = 'created_at', wip: str = None, approved: str = None):
    """
    Retrieves merge requests for a project with various filtering options. Allows users to search, filter, and sort merge requests based on criteria like state, assignees, reviewers, branches, and timeframes.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        state (str, optional): Filter by state (opened, closed, locked, merged, all)
        labels (str, optional): Comma-separated list of labels
        milestone (str, optional): Filter by milestone
        scope (str, optional): Filter by scope (created_by_me, assigned_to_me, all)
        author_username (str, optional): Filter by author username
        assignee_id (int, optional): Filter by assignee ID
        reviewer_username (str, optional): Filter by reviewer username
        created_after (str, optional): Filter by creation date after (ISO 8601 format)
        created_before (str, optional): Filter by creation date before (ISO 8601 format)
        source_branch (str, optional): Filter by source branch
        target_branch (str, optional): Filter by target branch
        search (str, optional): Search in title and description
        sort (str, optional): Sort direction (asc or desc)
        order_by (str, optional): Order by field (created_at, updated_at, title)
        wip (str, optional): Filter by draft status (yes or no)
        approved (str, optional): Filter by approval status (yes or no)
        
    Returns:
        Returns a list of project merge requests with detailed information including state, branches, authors, reviewers, timestamps, and approval status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Build endpoint URL
    endpoint = f"{base_url}/projects/{quote(str(project_id))}/merge_requests"
    
    # Build query parameters
    params = {}
    if state:
        params['state'] = state
    if labels:
        params['labels'] = labels
    if milestone:
        params['milestone'] = milestone
    if scope:
        params['scope'] = scope
    if author_username:
        params['author_username'] = author_username
    if assignee_id:
        params['assignee_id'] = assignee_id
    if reviewer_username:
        params['reviewer_username'] = reviewer_username
    if created_after:
        params['created_after'] = created_after
    if created_before:
        params['created_before'] = created_before
    if source_branch:
        params['source_branch'] = source_branch
    if target_branch:
        params['target_branch'] = target_branch
    if search:
        params['search'] = search
    if sort:
        params['sort'] = sort
    if order_by:
        params['order_by'] = order_by
    if wip:
        params['wip'] = wip
    if approved:
        params['approved'] = approved
    
    # Make the API request
    response = requests.get(endpoint, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = list_project_merge_requests(project_id=183, state='all', order_by='updated_at')
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