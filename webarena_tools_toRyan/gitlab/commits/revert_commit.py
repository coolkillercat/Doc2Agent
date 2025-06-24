import requests
from urllib.parse import quote

def revert_commit(project_id: str, commit_sha: str, branch: str, dry_run: bool = False):
    """
    Reverts a specific commit in a target branch of a GitLab project. Can perform a dry run to check if the revert would succeed without committing changes.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        commit_sha (str): Commit SHA to revert
        branch (str): Target branch name
        dry_run (bool, optional): If True, does not commit any changes. Defaults to False.
    
    Returns:
        requests.Response: The response from the API
        
    Example:
        >>> revert_commit(project_id="183", commit_sha="442ebddc23885ecf64d430e50d0df6b6e94e16a7", branch="main")
        >>> revert_commit(project_id="183", commit_sha="442ebddc23885ecf64d430e50d0df6b6e94e16a7", branch="main", dry_run=True)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits/{commit_sha}/revert"
    
    data = {
        'branch': branch
    }
    
    if dry_run:
        data['dry_run'] = dry_run
    
    return requests.post(url, headers=headers, json=data)

if __name__ == '__main__':
    r = revert_commit(project_id=183, commit_sha="a738f717824ff53aebad8b090c1b79a14f2bd9e8", branch="main")
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