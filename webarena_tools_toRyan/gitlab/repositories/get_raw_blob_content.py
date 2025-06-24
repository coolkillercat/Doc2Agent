import requests
from urllib.parse import quote

def get_raw_blob_content(project_id, blob_sha, base_url=None, token=None):
    """
    Retrieves the raw file contents of a specific blob from a project repository by its SHA.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        blob_sha (str): The blob SHA
        base_url (str, optional): The base URL for the GitLab API
        token (str, optional): The private token for authentication
        
    Returns:
        Returns the raw file contents of a specific blob from a project repository identified by its SHA.
    Example:
        >>> content = get_raw_blob_content(183, "08430979e9059811ca9d9389458f5fada420faa6")
        >>> print(content[:50])  # Print first 50 characters of the content
    """
    base_url = base_url or "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    token = token or "GITLAB_KEY_REMOVED"
    
    headers = {'PRIVATE-TOKEN': token}
    url = f"{base_url}/projects/{project_id}/repository/blobs/{blob_sha}/raw"
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.text

if __name__ == '__main__':
    r = get_raw_blob_content(project_id=183, blob_sha="08430979e9059811ca9d9389458f5fada420faa6")
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = r
    result_dict['json'] = r_json
    result_dict['content'] = r
    print(json.dumps(result_dict, indent=4))