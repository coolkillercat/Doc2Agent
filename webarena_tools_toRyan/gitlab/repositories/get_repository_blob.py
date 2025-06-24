import requests
from urllib.parse import quote

def get_repository_blob(project_id, sha):
    """
    Retrieve a blob (file content) from a repository. Returns blob information including size and Base64 encoded content.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        sha (str): The blob SHA (commit hash or reference to the blob)
        
    Returns:
        Returns blob information from a repository including size, encoding, content (Base64 encoded), and SHA.
    Example:
        >>> response = get_repository_blob(project_id=183, sha="08430979e9059811ca9d9389458f5fada420faa6")
        >>> print(response.status_code)
        200
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/blobs/{sha}"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_repository_blob(project_id=183, sha="08430979e9059811ca9d9389458f5fada420faa6")
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