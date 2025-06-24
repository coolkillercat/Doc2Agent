import requests, json
from urllib.parse import quote

def get_snippet_discussions(project_id, snippet_id, base_url=None, token=None):
    """
    Retrieves all discussion threads and comments for a specific project snippet, allowing users to review feedback and conversations related to the snippet.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        snippet_id (int): The ID of the snippet
        base_url (str, optional): The base URL of the GitLab API. Defaults to None.
        token (str, optional): The private token for authentication. Defaults to None.
        
    Returns:
        Response object containing the API response with all discussion threads and comments
        
    Example:
        >>> get_snippet_discussions(183, 1)
        <Response [200]>
    """
    if base_url is None:
        base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    if token is None:
        token = "GITLAB_KEY_REMOVED"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/projects/{project_id}/snippets/{snippet_id}/discussions"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_snippet_discussions(project_id=183, snippet_id=1)
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