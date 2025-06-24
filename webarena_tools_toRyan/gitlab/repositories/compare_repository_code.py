import requests, json
from urllib.parse import quote

def compare_repository_code(project_id: str, from_ref: str, to_ref: str, from_project_id: int = None, straight: bool = False, unidiff: bool = False) -> dict:
    """
    Compares code between two branches, tags, or commits in a GitLab repository, showing the differences between them.
    Useful for code reviews, tracking changes across branches, or identifying specific commits that introduced changes.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        from_ref (str): The commit SHA or branch name to compare from
        to_ref (str): The commit SHA or branch name to compare to
        from_project_id (int, optional): The ID to compare from. Defaults to None.
        straight (bool, optional): Comparison method: True for direct comparison, False to compare using merge base. Defaults to False.
        unidiff (bool, optional): Present diffs in the unified diff format. Defaults to False.
    
    Returns:
        dict: Response containing comparison details including commits and diffs
        
    Example:
        >>> compare_repository_code(project_id="183", from_ref="main", to_ref="master")
        # Returns comparison between main and master branches
        
        >>> compare_repository_code(project_id="183", from_ref="v1.0", to_ref="v2.0", straight=True)
        # Returns direct comparison between v1.0 and v2.0 tags
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/compare"
    
    params = {
        "from": from_ref,
        "to": to_ref,
        "straight": straight,
        "unidiff": unidiff
    }
    
    if from_project_id is not None:
        params["from_project_id"] = from_project_id
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == '__main__':
    r = compare_repository_code(project_id=183, from_ref="main", to_ref="master")
    r_json = None
    try:
        r_json = r
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))