import requests
from urllib.parse import quote

def get_merge_requests_by_commit(project_id, commit_sha, base_url="http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token="glpat-qvQ-N6mN_tAddXb2WWdi"):
    """
    Retrieves all merge requests associated with a specific commit in a project. This helps developers trace the origin of code changes and understand the context in which a commit was introduced.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        commit_sha (str): The commit SHA to lookup
        base_url (str, optional): The base URL for the GitLab API
        token (str, optional): The private token for authentication
        
    Returns:
        Response object: HTTP response from the GitLab API
        
    Example:
        >>> get_merge_requests_by_commit(183, "af5b13261899fb2c0db30abdd0af8b07cb44fdc5")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits/{commit_sha}/merge_requests"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_merge_requests_by_commit(project_id=183, commit_sha="af5b13261899fb2c0db30abdd0af8b07cb44fdc5")
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