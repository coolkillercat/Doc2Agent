import requests, json
from urllib.parse import quote



def create_commit(project_id: int|str, branch: str, commit_message: str, actions: list, start_branch: str = None, start_sha: str = None, start_project: int|str = None, author_email: str = None, author_name: str = None, stats: bool = True, force: bool = False):
    """
    Creates a commit with multiple file operations (create, update, move, delete, chmod) in a single transaction. This allows for complex repository changes to be bundled together with a single commit message.
    
    Args:
        project_id (int|str): The ID or URL-encoded path of the project
        branch (str): Name of the branch to commit into
        commit_message (str): Commit message
        actions (list): An array of action hashes to commit as a batch
        start_branch (str, optional): Name of the branch to start the new branch from
        start_sha (str, optional): SHA of the commit to start the new branch from
        start_project (int|str, optional): The project ID or path to start the new branch from
        author_email (str, optional): Specify the commit author's email address
        author_name (str, optional): Specify the commit author's name
        stats (bool, optional): Include commit stats. Default is True
        force (bool, optional): When True overwrites the target branch with a new commit based on start_branch or start_sha
    
    Returns:
        Returns commit details including ID, author information, timestamps, message, and optionally statistics about code changes."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/commits"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    payload = {
        "branch": branch,
        "commit_message": commit_message,
        "actions": actions,
        "stats": stats,
        "force": force
    }
    
    # Add optional parameters if provided
    if start_branch:
        payload["start_branch"] = start_branch
    if start_sha:
        payload["start_sha"] = start_sha
    if start_project:
        payload["start_project"] = start_project
    if author_email:
        payload["author_email"] = author_email
    if author_name:
        payload["author_name"] = author_name
    
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = create_commit(
        project_id=183,
        branch="main",
        commit_message="Add new test files and update existing ones",
        actions=[
            {
                "action": "create",
                "file_path": "docs/test.md",
                "content": "# Test Document\nThis is a test markdown document."
            },
            {
                "action": "update",
                "file_path": "README.md",
                "content": "# Updated Project\nThis README has been updated via the API."
            }
        ]
    )
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