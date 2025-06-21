import requests, json
from urllib.parse import quote



def get_commit(project_id: str, commit_sha: str, include_stats: bool = True):
    """
    Retrieves detailed information about a specific commit in a project repository, including author details, commit message, timestamps, and optionally statistics about code changes (additions/deletions).
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        commit_sha (str): The commit hash or name of a repository branch or tag
        include_stats (bool, optional): Whether to include commit stats. Defaults to True.
    
    Returns:
        Returns detailed information about a specific commit in a repository, including commit metadata, author details, timestamps, and optionally code change statistics."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL-encode the project_id to handle special characters
    encoded_project_id = quote(str(project_id), safe='')
    
    # Construct the URL
    url = f"{base_url}/projects/{encoded_project_id}/repository/commits/{commit_sha}"
    
    # Add stats parameter if needed
    params = {'stats': include_stats}
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_commit(project_id=183, commit_sha="main")
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