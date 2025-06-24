import requests, json
from urllib.parse import quote



def get_commit_dates(repo_id: str, commit_sha: str) -> dict:
    """
    Retrieves the date information for a specific commit in a GitLab repository, including created_at, committed_date, and authored_date fields for timestamp analysis and auditing.
    
    Args:
        repo_id (str): The ID or URL-encoded path of the project
        commit_sha (str): The commit hash or reference name
        
    Returns:
        Returns date information for a specific GitLab commit, including created_at, committed_date, and authored_date timestamps for auditing purposes."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(repo_id), safe='')}/repository/commits/{commit_sha}"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_commit_dates(repo_id=183, commit_sha="main")
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