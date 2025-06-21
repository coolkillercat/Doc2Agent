import requests, json
from urllib.parse import quote

def update_merge_request(project_id: str, merge_request_iid: int, title: str = None, description: str = None, target_branch: str = None, state_event: str = None, assignee_ids: list = None, reviewer_ids: list = None, labels: str = None, add_labels: str = None, remove_labels: str = None, milestone_id: int = None, squash: bool = None, remove_source_branch: bool = None, discussion_locked: bool = None, allow_collaboration: bool = None):
    """
    Updates an existing merge request with specified attributes such as title, target branch, assignees, labels, or state (close/reopen). Allows for customizing various aspects of a merge request to reflect current development status and requirements.
    
    Args:
        project_id: The ID or URL-encoded path of the project
        merge_request_iid: The ID of the merge request to update
        title: New title for the merge request
        description: New description for the merge request
        target_branch: The target branch to change to
        state_event: New state (close/reopen)
        assignee_ids: List of user IDs to assign to the merge request
        reviewer_ids: List of user IDs to set as reviewers
        labels: Comma-separated label names (replaces existing labels)
        add_labels: Comma-separated label names to add
        remove_labels: Comma-separated label names to remove
        milestone_id: The ID of a milestone to assign
        squash: Whether the merge request should be squashed
        remove_source_branch: Whether to remove source branch when merging
        discussion_locked: Whether to lock discussions
        allow_collaboration: Allow commits from members who can merge to target branch
        
    Returns:
        Response object from the API call
        
    Examples:
        >>> update_merge_request(project_id=183, merge_request_iid=20, title="Updated MR Title")
        >>> update_merge_request(project_id=183, merge_request_iid=20, description="This is an updated description", add_labels="bug,enhancement")
        >>> update_merge_request(project_id=183, merge_request_iid=20, target_branch="main", state_event="close")
        >>> update_merge_request(project_id=183, merge_request_iid=20, assignee_ids=[2330], reviewer_ids=[2330])
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}"
    
    data = {}
    if title is not None:
        data['title'] = title
    if description is not None:
        data['description'] = description
    if target_branch is not None:
        data['target_branch'] = target_branch
    if state_event is not None:
        data['state_event'] = state_event
    if assignee_ids is not None:
        data['assignee_ids'] = assignee_ids
    if reviewer_ids is not None:
        data['reviewer_ids'] = reviewer_ids
    if labels is not None:
        data['labels'] = labels
    if add_labels is not None:
        data['add_labels'] = add_labels
    if remove_labels is not None:
        data['remove_labels'] = remove_labels
    if milestone_id is not None:
        data['milestone_id'] = milestone_id
    if squash is not None:
        data['squash'] = squash
    if remove_source_branch is not None:
        data['remove_source_branch'] = remove_source_branch
    if discussion_locked is not None:
        data['discussion_locked'] = discussion_locked
    if allow_collaboration is not None:
        data['allow_collaboration'] = allow_collaboration
    
    response = requests.put(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = update_merge_request(project_id=183, merge_request_iid=1, title="Updated MR Title", description="This is an updated description", add_labels="bug,enhancement")
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