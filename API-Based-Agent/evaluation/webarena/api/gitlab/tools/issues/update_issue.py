import requests, json
from urllib.parse import quote



def update_issue(project_id: str, issue_iid: int, title: str = None, description: str = None, state_event: str = None, assignee_ids: list = None, labels: str = None, add_labels: str = None, remove_labels: str = None, milestone_id: int = None, due_date: str = None, confidential: bool = None, discussion_locked: bool = None, issue_type: str = None, weight: int = None, epic_id: int = None):
    """
    Updates an existing project issue with specified attributes. Can be used to modify issue details, change state (close/reopen), assign users, manage labels, set milestones, or update other issue properties.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the issue to update
        title (str, optional): The title of the issue
        description (str, optional): The description of the issue
        state_event (str, optional): Use 'close' to close the issue or 'reopen' to reopen it
        assignee_ids (list, optional): List of user IDs to assign the issue to
        labels (str, optional): Comma-separated label names. Set empty string to unassign all labels
        add_labels (str, optional): Comma-separated label names to add to the issue
        remove_labels (str, optional): Comma-separated label names to remove from the issue
        milestone_id (int, optional): The ID of a milestone to assign. Set to 0 to unassign
        due_date (str, optional): Due date in format YYYY-MM-DD
        confidential (bool, optional): Set to True to make the issue confidential
        discussion_locked (bool, optional): Set to True to lock discussions
        issue_type (str, optional): Type of issue ('issue', 'incident', 'test_case', or 'task')
        weight (int, optional): The weight of the issue (Premium/Ultimate only)
        epic_id (int, optional): ID of the epic to add the issue to (Premium/Ultimate only)
        
    Returns:
        Returns comprehensive details about the updated issue including its metadata, state, assignees, labels, time statistics, and related references."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/issues/{issue_iid}"
    
    payload = {}
    
    # Add parameters to payload if they are provided
    if title is not None:
        payload['title'] = title
    if description is not None:
        payload['description'] = description
    if state_event is not None:
        payload['state_event'] = state_event
    if assignee_ids is not None:
        payload['assignee_ids'] = assignee_ids
    if labels is not None:
        payload['labels'] = labels
    if add_labels is not None:
        payload['add_labels'] = add_labels
    if remove_labels is not None:
        payload['remove_labels'] = remove_labels
    if milestone_id is not None:
        payload['milestone_id'] = milestone_id
    if due_date is not None:
        payload['due_date'] = due_date
    if confidential is not None:
        payload['confidential'] = confidential
    if discussion_locked is not None:
        payload['discussion_locked'] = discussion_locked
    if issue_type is not None:
        payload['issue_type'] = issue_type
    if weight is not None:
        payload['weight'] = weight
    if epic_id is not None:
        payload['epic_id'] = epic_id
    
    return requests.put(url, headers=headers, json=payload)

if __name__ == '__main__':
    r = update_issue(project_id=183, issue_iid=1, title="Updated Issue Title", description="This is an updated description", state_event="close")
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