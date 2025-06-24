import requests, json
from urllib.parse import quote



def create_repository_file(project_id: int or str, file_path: str, content: str, branch: str, commit_message: str, author_name: str = None, author_email: str = None, encoding: str = 'text', execute_filemode: bool = None, start_branch: str = None):
    """
    Creates a new file in a repository with the specified content. Allows setting author information, encoding, and file execution permissions.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        file_path (str): URL-encoded full path to new file
        content (str): The file's content
        branch (str): Name of the branch to create the file in
        commit_message (str): The commit message
        author_name (str, optional): The commit author's name
        author_email (str, optional): The commit author's email address
        encoding (str, optional): Change encoding to 'base64'. Default is 'text'
        execute_filemode (bool, optional): Enables or disables the execute flag on the file
        start_branch (str, optional): Name of the base branch to create the new branch from
        
    Returns:
        Returns information about the newly created file including its path and the branch it was created in."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{project_id}/repository/files/{quote(file_path, safe='')}"
    
    payload = {
        'branch': branch,
        'commit_message': commit_message,
        'content': content
    }
    
    if author_name:
        payload['author_name'] = author_name
    
    if author_email:
        payload['author_email'] = author_email
    
    if encoding:
        payload['encoding'] = encoding
    
    if execute_filemode is not None:
        payload['execute_filemode'] = execute_filemode
    
    if start_branch:
        payload['start_branch'] = start_branch
    
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = create_repository_file(
        project_id=183,
        file_path="test/example.txt",
        content="This is a test file created using the API",
        branch="main",
        commit_message="Add test file via API",
        author_name="ByteBlaze",
        author_email="byteblaze@example.com"
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