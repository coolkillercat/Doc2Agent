import requests, json
from urllib.parse import quote



def create_project_issue(project_id: int, title: str, description: str = None, assignee_ids: list = None, confidential: bool = False, due_date: str = None, labels: str = None, milestone_id: int = None, issue_type: str = 'issue', weight: int = None, epic_id: int = None):
    """
    Creates a new issue in a GitLab project with customizable properties such as title, description, assignees, and other attributes. Allows users to track tasks, bugs, and feature requests within their project workflow.
    
    Args:
        project_id (int): The ID of the project where the issue will be created
        title (str): The title of the issue
        description (str, optional): The description of the issue
        assignee_ids (list, optional): List of user IDs to assign the issue to
        confidential (bool, optional): Set to True to make the issue confidential
        due_date (str, optional): Due date in YYYY-MM-DD format
        labels (str, optional): Comma-separated label names
        milestone_id (int, optional): The global ID of a milestone to assign
        issue_type (str, optional): Type of issue: 'issue', 'incident', 'test_case', or 'task'
        weight (int, optional): The weight of the issue (Premium/Ultimate only)
        epic_id (int, optional): ID of the epic to add the issue to (Premium/Ultimate only)
        
    Returns:
        Returns comprehensive issue details including ID, title, description, state, assignees, author information, time statistics, and related metadata for a newly created project issue."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/issues"
    
    payload = {
        "title": title
    }
    
    if description:
        payload["description"] = description
    if assignee_ids:
        payload["assignee_ids"] = assignee_ids
    if confidential:
        payload["confidential"] = confidential
    if due_date:
        payload["due_date"] = due_date
    if labels:
        payload["labels"] = labels
    if milestone_id:
        payload["milestone_id"] = milestone_id
    if issue_type:
        payload["issue_type"] = issue_type
    if weight is not None:
        payload["weight"] = weight
    if epic_id is not None:
        payload["epic_id"] = epic_id
        
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = create_project_issue(
        project_id=183, 
        title="Bug in login feature",
        description="Users are unable to login using OAuth credentials",
        labels="bug,critical",
        issue_type="issue",
        confidential=False
    )
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