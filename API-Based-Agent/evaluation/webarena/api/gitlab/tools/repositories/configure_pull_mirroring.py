import requests, json
from urllib.parse import quote

def configure_pull_mirroring(project_id: int, import_url: str, mirror: bool = True, mirror_trigger_builds: bool = False, only_mirror_protected_branches: bool = False, mirror_branch_regex: str = None):
    """
    Configures pull mirroring for a GitLab project, allowing automatic synchronization from an external repository.
    
    Args:
        project_id (int): The ID of the project to configure pull mirroring for
        import_url (str): URL of remote repository being mirrored (with user:token if needed)
        mirror (bool, optional): Enables pull mirroring on project when set to True. Defaults to True.
        mirror_trigger_builds (bool, optional): Trigger pipelines for mirror updates when set to True. Defaults to False.
        only_mirror_protected_branches (bool, optional): Limits mirroring to only protected branches when set to True. Defaults to False.
        mirror_branch_regex (str, optional): Regular expression for branch name matching. Only branches matching this regex will be mirrored. Defaults to None.
    
    Returns:
        requests.Response: The response from the API
        
    Example:
        >>> configure_pull_mirroring(
        ...     project_id=183,
        ...     import_url="https://username:token@gitlab.example.com/group/project.git",
        ...     mirror=True,
        ...     mirror_trigger_builds=True,
        ...     only_mirror_protected_branches=False,
        ...     mirror_branch_regex="^(main|develop)$"
        ... )
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}"
    
    data = {
        "mirror": mirror,
        "import_url": import_url
    }
    
    if mirror_trigger_builds is not None:
        data["mirror_trigger_builds"] = mirror_trigger_builds
        
    if only_mirror_protected_branches is not None:
        data["only_mirror_protected_branches"] = only_mirror_protected_branches
        
    if mirror_branch_regex is not None:
        data["mirror_branch_regex"] = mirror_branch_regex
    
    response = requests.put(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = configure_pull_mirroring(
        project_id=183,
        import_url="https://username:token@gitlab.example.com/group/project.git",
        mirror=True,
        mirror_trigger_builds=True,
        only_mirror_protected_branches=False,
        mirror_branch_regex="^(main|develop)$"
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