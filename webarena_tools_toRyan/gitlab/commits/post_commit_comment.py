import requests, json
from urllib.parse import quote



def post_commit_comment(project_id: str, commit_sha: str, note: str, path: str = None, line: int = None, line_type: str = None):
    """
    Adds a comment to a specific commit. Can optionally target a specific line in a specific file of the commit for contextual feedback.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        commit_sha (str): The commit SHA or name of a repository branch or tag
        note (str): The text of the comment
        path (str, optional): The file path relative to the repository
        line (int, optional): The line number where the comment should be placed
        line_type (str, optional): The line type. Takes 'new' or 'old' as arguments
        
    Returns:
        Returns commit comment details including the note content, file path information, line references, and author metadata."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits/{quote(str(commit_sha), safe='')}/comments"
    
    data = {'note': note}
    
    if path:
        data['path'] = path
    if line:
        data['line'] = line
    if line_type:
        data['line_type'] = line_type
    
    return requests.post(url, headers=headers, json=data)

if __name__ == '__main__':
    r = post_commit_comment(project_id=183, commit_sha="main", note="This is a test comment on the main branch")
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