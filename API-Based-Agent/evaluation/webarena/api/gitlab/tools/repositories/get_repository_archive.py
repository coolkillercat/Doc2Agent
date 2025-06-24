import requests
from urllib.parse import quote

def get_repository_archive(project_id, sha=None, path='', format='tar.gz'):
    """
    Downloads an archive of a repository or a specific subpath within it. Allows specifying a particular commit, tag, or branch reference, and choosing the archive format.
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project
        sha (str, optional): The commit SHA, tag, or branch reference to download. Defaults to None (tip of default branch).
        path (str, optional): The subpath of the repository to download. Defaults to empty string (whole repository).
        format (str, optional): Format of the archive. Options include 'tar.gz', 'zip', 'tar', 'tar.bz2', etc. Defaults to 'tar.gz'.
        
    Returns:
        Returns a downloadable archive of a repository or specific subpath in a chosen format (such as tar.gz or zip).
    Example:
        >>> response = get_repository_archive(project_id=183, sha="main", format="zip")
        >>> with open("repo_archive.zip", "wb") as f:
        ...     f.write(response.content)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/archive.{format}"
    
    params = {}
    if sha:
        params['sha'] = sha
    if path:
        params['path'] = path
        
    response = requests.get(url, headers=headers, params=params, stream=True)
    return response

if __name__ == '__main__':
    r = get_repository_archive(project_id=183, sha="main", path="", format="zip")
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
    # Binary content should not be decoded as UTF-8
    result_dict['content'] = "Binary content (archive file)"
    print(json.dumps(result_dict, indent=4))