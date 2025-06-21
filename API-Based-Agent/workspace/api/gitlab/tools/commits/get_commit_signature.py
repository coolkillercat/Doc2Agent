import requests, json
from urllib.parse import quote


def get_commit_signature(project_id, commit_sha, base_url="http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", private_token="glpat-qvQ-N6mN_tAddXb2WWdi"):
    """
    Retrieves the digital signature information for a specific commit in a project repository.
    
    This function fetches signature verification status, type (PGP, SSH, or X509), and signer details
    if the commit is signed. For unsigned commits, it will return a 404 response.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        commit_sha (str): The commit hash or name of a repository branch or tag
        base_url (str, optional): The base URL for the GitLab API
        private_token (str, optional): The private token for authentication
        
    Returns:
        Response object: The HTTP response from the API
        
    Examples:
        >>> response = get_commit_signature(183, "442ebddc23885ecf64d430e50d0df6b6e94e16a7")
        >>> response = get_commit_signature("my-group/my-project", "main")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': private_token}
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits/{quote(str(commit_sha), safe='')}/signature"
    
    response = requests.get(url, headers=headers)
    return response


if __name__ == '__main__':
    r = get_commit_signature(project_id=183, commit_sha="main")
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