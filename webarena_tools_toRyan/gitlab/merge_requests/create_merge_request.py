import requests, json
from urllib.parse import quote


def create_merge_request(source_branch: str, target_branch: str, title: str, description: str = '', project_id: int = None, remove_source_branch: bool = False, squash: bool = False, labels: list = None, milestone_id: int = None, assignee_ids: list = None, reviewer_ids: list = None):
    """
    Creates a new merge request between two branches. Note that certain fields like diff_refs and changes_count will be populated asynchronously after creation.
    
    Args:
        source_branch (str): The source branch name
        target_branch (str): The target branch name
        title (str): Title of the merge request
        description (str, optional): Description of the merge request. Defaults to ''.
        project_id (int, optional): ID of the project. Defaults to None.
        remove_source_branch (bool, optional): Flag to remove source branch when merge request is accepted. Defaults to False.
        squash (bool, optional): Flag to squash commits when merge request is accepted. Defaults to False.
        labels (list, optional): Labels to assign to the merge request. Defaults to None.
        milestone_id (int, optional): The milestone ID to assign. Defaults to None.
        assignee_ids (list, optional): List of user IDs to assign as assignees. Defaults to None.
        reviewer_ids (list, optional): List of user IDs to assign as reviewers. Defaults to None.
    
    Returns:
        requests.Response: The API response object
        
    Example:
        >>> create_merge_request(
        ...     source_branch="feature-branch",
        ...     target_branch="main",
        ...     title="Add new feature",
        ...     description="This merge request adds a new feature",
        ...     project_id=183,
        ...     remove_source_branch=True,
        ...     assignee_ids=[2330]
        ... )
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{project_id}/merge_requests"
    
    data = {
        "source_branch": source_branch,
        "target_branch": target_branch,
        "title": title,
        "description": description,
        "remove_source_branch": remove_source_branch,
        "squash": squash
    }
    
    if labels:
        if isinstance(labels, list):
            data["labels"] = ",".join(labels)
        else:
            data["labels"] = labels
    
    if milestone_id:
        data["milestone_id"] = milestone_id
    
    if assignee_ids:
        data["assignee_ids"] = assignee_ids
    
    if reviewer_ids:
        data["reviewer_ids"] = reviewer_ids
    
    response = requests.post(url, headers=headers, json=data)
    return response


if __name__ == '__main__':
    r = create_merge_request(
        source_branch="feature-branch",
        target_branch="main",
        title="Add new feature",
        description="This merge request adds a new feature",
        project_id=183,
        remove_source_branch=True,
        assignee_ids=[2330]
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