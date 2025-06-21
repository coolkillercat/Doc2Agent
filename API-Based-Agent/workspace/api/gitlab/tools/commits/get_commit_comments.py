import requests, json
from urllib.parse import quote



def get_commit_comments(project_id: str, commit_sha: str):
    """
    Retrieves all comments associated with a specific commit in a GitLab project. Useful for code review workflows and tracking feedback on changes.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        commit_sha (str): The commit hash or name of a repository branch or tag
        
    Returns:
        Returns comments made on a specific commit in a GitLab project, including the comment text and author information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits/{quote(str(commit_sha), safe='')}/comments"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_commit_comments(project_id=183, commit_sha="main")
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