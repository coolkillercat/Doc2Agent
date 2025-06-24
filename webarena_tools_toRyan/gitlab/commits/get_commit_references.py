import requests, json
from urllib.parse import quote


def get_commit_references(project_id, commit_sha, ref_type='all', page=1, per_page=20):
    """
    Retrieves all references (branches or tags) that a specific commit is pushed to, allowing users to track which branches and tags contain a particular commit.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        commit_sha (str): The commit hash
        ref_type (str, optional): The scope of commits. Possible values 'branch', 'tag', 'all'. Default is 'all'.
        page (int, optional): Page number for pagination. Default is 1.
        per_page (int, optional): Number of items per page. Default is 20.
        
    Returns:
        requests.Response: The API response containing references the commit is pushed to
        
    Example:
        >>> get_commit_references(183, "442ebddc23885ecf64d430e50d0df6b6e94e16a7")
        >>> get_commit_references(183, "442ebddc23885ecf64d430e50d0df6b6e94e16a7", ref_type="branch")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits/{commit_sha}/refs"
    
    params = {
        'type': ref_type,
        'page': page,
        'per_page': per_page
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_commit_references(project_id=183, commit_sha="5937ac0a7beb003549fc5fd26fc247adbce4a52e", ref_type="all")
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