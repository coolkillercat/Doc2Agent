import requests, json
from urllib.parse import quote



def create_project(name: str, path: str = None, description: str = None, namespace_id: int = None, visibility: str = None, initialize_with_readme: bool = False, topics: list = None, default_branch: str = None, merge_method: str = None, ci_config_path: str = None, lfs_enabled: bool = None, wiki_access_level: str = None, issues_access_level: str = None, merge_requests_access_level: str = None, builds_access_level: str = None):
    """
    Creates a new GitLab project with customizable settings including name, path, visibility, and various access controls. This tool streamlines project creation while allowing fine-grained configuration of repository features.
    
    Args:
        name (str): The name of the new project.
        path (str, optional): Repository name for new project. Generated based on name if not provided.
        description (str, optional): Short project description.
        namespace_id (int, optional): Namespace for the new project (defaults to the current user's namespace).
        visibility (str, optional): Project visibility level - 'private', 'internal', or 'public'.
        initialize_with_readme (bool, optional): Whether to create a Git repository with just a README.md file. Default is False.
        topics (list, optional): The list of topics for a project.
        default_branch (str, optional): The default branch name. Requires initialize_with_readme to be True.
        merge_method (str, optional): Set the merge method used.
        ci_config_path (str, optional): The path to CI configuration file.
        lfs_enabled (bool, optional): Enable LFS.
        wiki_access_level (str, optional): One of 'disabled', 'private', or 'enabled'.
        issues_access_level (str, optional): One of 'disabled', 'private', or 'enabled'.
        merge_requests_access_level (str, optional): One of 'disabled', 'private', or 'enabled'.
        builds_access_level (str, optional): One of 'disabled', 'private', or 'enabled'.
        
    Returns:
        Returns comprehensive details about a newly created GitLab project including its metadata, repository URLs, access settings, and configuration options."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects"
    
    payload = {
        "name": name
    }
    
    if path:
        payload["path"] = path
    if description:
        payload["description"] = description
    if namespace_id:
        payload["namespace_id"] = namespace_id
    if visibility:
        payload["visibility"] = visibility
    if initialize_with_readme:
        payload["initialize_with_readme"] = initialize_with_readme
    if topics:
        payload["topics"] = topics
    if default_branch and initialize_with_readme:
        payload["default_branch"] = default_branch
    if merge_method:
        payload["merge_method"] = merge_method
    if ci_config_path:
        payload["ci_config_path"] = ci_config_path
    if lfs_enabled is not None:
        payload["lfs_enabled"] = lfs_enabled
    if wiki_access_level:
        payload["wiki_access_level"] = wiki_access_level
    if issues_access_level:
        payload["issues_access_level"] = issues_access_level
    if merge_requests_access_level:
        payload["merge_requests_access_level"] = merge_requests_access_level
    if builds_access_level:
        payload["builds_access_level"] = builds_access_level
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response

if __name__ == '__main__':
    r = create_project(
        name="Test Project", 
        description="A test project created via API", 
        visibility="private", 
        initialize_with_readme=True, 
        topics=["test", "api"]
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