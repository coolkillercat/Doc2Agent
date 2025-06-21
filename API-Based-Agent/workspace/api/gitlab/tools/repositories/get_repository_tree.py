import requests, json
from urllib.parse import quote



def get_repository_tree(project_id: str, path: str = None, recursive: bool = False, ref: str = None, per_page: int = 20, pagination: str = None, page_token: str = None):
    """
    Retrieves a list of files and directories in a GitLab project repository. Useful for exploring repository structure, locating specific files or directories, and supporting file browser functionality in applications.
    
    Args:
        project_id: The ID or URL-encoded path of the project.
        path: The path inside the repository to get content of subdirectories.
        recursive: Boolean value to get a recursive tree. Default is False.
        ref: The name of a repository branch or tag or default branch if not specified.
        per_page: Number of results to show per page. Default is 20.
        pagination: If 'keyset', use the keyset-based pagination method.
        page_token: The tree record ID at which to fetch the next page.
        
    Returns:
        Returns a list of files and directories in a GitLab project repository with their identifiers, names, types, paths, and access modes."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/tree"
    
    params = {}
    if path:
        params['path'] = path
    if recursive:
        params['recursive'] = recursive
    if ref:
        params['ref'] = ref
    if per_page:
        params['per_page'] = per_page
    if pagination:
        params['pagination'] = pagination
    if page_token:
        params['page_token'] = page_token
        
    return requests.get(url, headers=headers, params=params)

if __name__ == '__main__':
    r = get_repository_tree(project_id=183, path='', recursive=False)
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