import requests, json
from urllib.parse import quote


def list_group_merge_requests(group_id: str, state: str = None, milestone: str = None, labels: str = None, 
                             author_id: int = None, author_username: str = None, assignee_id: int = None, 
                             reviewer_id: int = None, reviewer_username: str = None, scope: str = None, 
                             search: str = None, source_branch: str = None, target_branch: str = None, 
                             created_after: str = None, created_before: str = None, updated_after: str = None, 
                             updated_before: str = None, sort: str = 'desc', order_by: str = 'created_at', 
                             view: str = None, with_labels_details: bool = False, approved_by_ids: list = None,
                             approved_by_usernames: list = None, approver_ids: list = None, approved: str = None,
                             merge_user_id: int = None, merge_user_username: str = None, my_reaction_emoji: str = None,
                             non_archived: bool = True, page: int = None, per_page: int = None):
    """
    Retrieves merge requests for a specified group and its subgroups with customizable filtering options.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        state (str, optional): Filter by state ('opened', 'closed', 'locked', 'merged', or 'all')
        milestone (str, optional): Filter by milestone name. Use 'None' for no milestone, 'Any' for any milestone.
        labels (str, optional): Comma-separated list of label names. Use 'None' for no labels, 'Any' for any labels.
        author_id (int, optional): Filter by author ID
        author_username (str, optional): Filter by author username (mutually exclusive with author_id)
        assignee_id (int, optional): Filter by assignee ID. Use 'None' for unassigned, 'Any' for any assignee.
        reviewer_id (int, optional): Filter by reviewer ID. Use 'None' for no reviewers, 'Any' for any reviewer.
        reviewer_username (str, optional): Filter by reviewer username (mutually exclusive with reviewer_id)
        scope (str, optional): Filter by scope ('created_by_me', 'assigned_to_me', or 'all')
        search (str, optional): Search merge requests against title and description
        source_branch (str, optional): Filter by source branch
        target_branch (str, optional): Filter by target branch
        created_after (str, optional): Filter by creation date after (ISO 8601 format: '2019-03-15T08:00:00Z')
        created_before (str, optional): Filter by creation date before (ISO 8601 format: '2019-03-15T08:00:00Z')
        updated_after (str, optional): Filter by update date after (ISO 8601 format: '2019-03-15T08:00:00Z')
        updated_before (str, optional): Filter by update date before (ISO 8601 format: '2019-03-15T08:00:00Z')
        sort (str, optional): Sort order ('asc' or 'desc', default is 'desc')
        order_by (str, optional): Order by field ('created_at', 'title', or 'updated_at', default is 'created_at')
        view (str, optional): If 'simple', returns basic state of merge requests
        with_labels_details (bool, optional): If True, returns more details for each label
        approved_by_ids (list, optional): Filter by approval from specific user IDs
        approved_by_usernames (list, optional): Filter by approval from specific usernames
        approver_ids (list, optional): Filter by specific approver IDs
        approved (str, optional): Filter by approval status ('yes' or 'no')
        merge_user_id (int, optional): Filter by user who merged the MR
        merge_user_username (str, optional): Filter by username who merged the MR
        my_reaction_emoji (str, optional): Filter by reaction emoji
        non_archived (bool, optional): If True, returns MRs from non-archived projects only
        page (int, optional): Page number for pagination
        per_page (int, optional): Number of items per page
        
    Returns:
        requests.Response: API response containing merge requests
        
    Example:
        >>> response = list_group_merge_requests(group_id='183', state='opened')
        >>> response = list_group_merge_requests(group_id='183', author_username='byteblaze', labels='bug,enhancement')
        >>> response = list_group_merge_requests(group_id='183', milestone='v2.0', sort='asc', order_by='updated_at')
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{quote(str(group_id), safe='')}/merge_requests"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    params = {}
    if state:
        params['state'] = state
    if milestone:
        params['milestone'] = milestone
    if labels:
        params['labels'] = labels
    if author_id:
        params['author_id'] = author_id
    if author_username:
        params['author_username'] = author_username
    if assignee_id:
        params['assignee_id'] = assignee_id
    if reviewer_id:
        params['reviewer_id'] = reviewer_id
    if reviewer_username:
        params['reviewer_username'] = reviewer_username
    if scope:
        params['scope'] = scope
    if search:
        params['search'] = search
    if source_branch:
        params['source_branch'] = source_branch
    if target_branch:
        params['target_branch'] = target_branch
    if created_after:
        params['created_after'] = created_after
    if created_before:
        params['created_before'] = created_before
    if updated_after:
        params['updated_after'] = updated_after
    if updated_before:
        params['updated_before'] = updated_before
    if sort:
        params['sort'] = sort
    if order_by:
        params['order_by'] = order_by
    if view:
        params['view'] = view
    if with_labels_details is not None:
        params['with_labels_details'] = with_labels_details
    if approved_by_ids:
        params['approved_by_ids'] = approved_by_ids
    if approved_by_usernames:
        params['approved_by_usernames'] = approved_by_usernames
    if approver_ids:
        params['approver_ids'] = approver_ids
    if approved:
        params['approved'] = approved
    if merge_user_id:
        params['merge_user_id'] = merge_user_id
    if merge_user_username:
        params['merge_user_username'] = merge_user_username
    if my_reaction_emoji:
        params['my_reaction_emoji'] = my_reaction_emoji
    if non_archived is not None:
        params['non_archived'] = non_archived
    if page:
        params['page'] = page
    if per_page:
        params['per_page'] = per_page
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_group_merge_requests(group_id='183', state='all')
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