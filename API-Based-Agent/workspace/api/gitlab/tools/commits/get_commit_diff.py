import requests, json
from urllib.parse import quote



def get_commit_diff(project_id: str, commit_sha: str, unidiff: bool = False) -> list:
    """
    Retrieves the diff of a specific commit in a GitLab project, showing file changes between the commit and its parent. Useful for code review, change analysis, and understanding repository modifications.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        commit_sha (str): The commit hash or name of a repository branch or tag
        unidiff (bool, optional): Present diffs in the unified diff format. Defaults to False.
    
    Returns:
        Returns a list of file changes in a specific commit, including the diff content, file paths, and modification status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits/{quote(str(commit_sha), safe='')}/diff"
    
    params = {}
    if unidiff:
        params['unidiff'] = 'true'
    
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_commit_diff(project_id=183, commit_sha='main', unidiff=False)
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