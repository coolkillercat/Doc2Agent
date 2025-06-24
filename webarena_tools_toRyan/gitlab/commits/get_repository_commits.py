import requests, json
from urllib.parse import quote



def get_repository_commits(project_id: str, ref_name: str = None, path: str = None, since: str = None, until: str = None, limit: int = None) -> list:
    """
    Retrieves a list of commits from a repository with filtering options by reference, file path, and date range. Useful for developers tracking project history and changes.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        ref_name (str, optional): The name of a repository branch, tag, or commit
        path (str, optional): The file path to filter commits by
        since (str, optional): Only commits after or on this date will be returned (ISO 8601 format)
        until (str, optional): Only commits before or on this date will be returned (ISO 8601 format)
        limit (int, optional): Maximum number of commits to return
        
    Returns:
        Returns a list of repository commits with metadata including commit ID, author information, timestamps, and commit messages."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits"
    
    params = {}
    if ref_name:
        params['ref_name'] = ref_name
    if path:
        params['path'] = path
    if since:
        params['since'] = since
    if until:
        params['until'] = until
    if limit:
        params['per_page'] = limit
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_repository_commits(project_id=183, ref_name='main', limit=5)
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