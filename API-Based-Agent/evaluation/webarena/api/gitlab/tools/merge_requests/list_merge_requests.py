import requests, json
from urllib.parse import quote



def list_merge_requests(state: str = None, scope: str = 'created_by_me', labels: str = None, milestone: str = None, author_id: int = None, author_username: str = None, assignee_id: int = None, reviewer_id: int = None, search: str = None, in_scope: str = None, source_branch: str = None, target_branch: str = None, sort: str = 'desc', order_by: str = 'created_at', created_after: str = None, created_before: str = None, updated_after: str = None, updated_before: str = None, wip: str = None, with_labels_details: bool = False):
    """
    Retrieves merge requests based on specified filters, allowing users to find MRs by state, assignee, reviewer, branch, and other attributes. Useful for tracking work in progress, reviewing code contributions, or monitoring merge request status.
    
    Returns:
        Returns a list of merge requests with detailed information including ID, title, state, branches, author details, and merge status.
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/merge_requests"
    
    params = {}
    
    if state:
        params['state'] = state
    if scope:
        params['scope'] = scope
    if labels:
        params['labels'] = labels
    if milestone:
        params['milestone'] = milestone
    if author_id:
        params['author_id'] = author_id
    if author_username:
        params['author_username'] = author_username
    if assignee_id:
        params['assignee_id'] = assignee_id
    if reviewer_id:
        params['reviewer_id'] = reviewer_id
    if search:
        params['search'] = search
    if in_scope:
        params['in'] = in_scope
    if source_branch:
        params['source_branch'] = source_branch
    if target_branch:
        params['target_branch'] = target_branch
    if sort:
        params['sort'] = sort
    if order_by:
        params['order_by'] = order_by
    if created_after:
        params['created_after'] = created_after
    if created_before:
        params['created_before'] = created_before
    if updated_after:
        params['updated_after'] = updated_after
    if updated_before:
        params['updated_before'] = updated_before
    if wip is not None:
        params['wip'] = wip
    if with_labels_details:
        params['with_labels_details'] = with_labels_details
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_merge_requests(scope='all', state='opened', author_id=2330)
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