import requests
from urllib.parse import quote

def cherry_pick_commit(project_id: int, commit_sha: str, target_branch: str, dry_run: bool = False, custom_message: str = None):
    """
    Cherry-picks a specified commit to a target branch in a GitLab project. Allows for dry run testing and customizing the commit message.
    
    Args:
        project_id (int): The ID of the GitLab project
        commit_sha (str): The commit hash to cherry-pick
        target_branch (str): The name of the branch to cherry-pick to
        dry_run (bool, optional): If True, tests the cherry-pick without committing changes. Defaults to False.
        custom_message (str, optional): A custom commit message for the new commit. Defaults to None.
        
    Returns:
        requests.Response: The HTTP response from the API
        
    Example:
        >>> cherry_pick_commit(
        ...     project_id=183,
        ...     commit_sha="442ebddc23885ecf64d430e50d0df6b6e94e16a7",
        ...     target_branch="main",
        ...     dry_run=True,
        ...     custom_message="Cherry-picked feature commit"
        ... )
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/repository/commits/{commit_sha}/cherry_pick"
    
    data = {
        "branch": target_branch
    }
    
    if dry_run:
        data["dry_run"] = dry_run
    
    if custom_message:
        data["message"] = custom_message
    
    return requests.post(url, headers=headers, json=data)

if __name__ == '__main__':
    r = cherry_pick_commit(project_id=183, commit_sha="main", target_branch="develop", dry_run=True)
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