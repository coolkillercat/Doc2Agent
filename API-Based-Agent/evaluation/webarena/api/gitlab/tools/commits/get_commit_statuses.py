import requests, json
from urllib.parse import quote

def get_commit_statuses(project_id: int, commit_sha: str, ref: str = None, stage: str = None, name: str = None, all_statuses: bool = False):
    """
    Retrieves the statuses of a specific commit in a GitLab project. This helps developers monitor the build, test, and deployment status of their code changes.
    
    Args:
        project_id (int): The ID of the project
        commit_sha (str): The commit SHA
        ref (str, optional): The name of a repository branch or tag
        stage (str, optional): Filter by build stage
        name (str, optional): Filter by job name
        all_statuses (bool, optional): Return all statuses, not only the latest ones
        
    Returns:
        Response object with commit statuses
        
    Example:
        >>> get_commit_statuses(project_id=183, commit_sha="18f3e63d05582537db6d183d9d557be09e1f90c8")
        >>> get_commit_statuses(project_id=183, commit_sha="18f3e63d05582537db6d183d9d557be09e1f90c8", ref="main", stage="test", name="bundler:audit", all_statuses=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/repository/commits/{commit_sha}/statuses"
    
    params = {}
    if ref:
        params['ref'] = ref
    if stage:
        params['stage'] = stage
    if name:
        params['name'] = name
    if all_statuses:
        params['all'] = all_statuses
        
    return requests.get(url, headers=headers, params=params)

if __name__ == '__main__':
    r = get_commit_statuses(project_id=183, commit_sha="18f3e63d05582537db6d183d9d557be09e1f90c8")
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