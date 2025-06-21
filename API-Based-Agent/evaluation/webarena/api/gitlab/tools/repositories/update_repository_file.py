import requests, json
from urllib.parse import quote



def update_repository_file(project_id, file_path, content, branch, commit_message, author_name=None, author_email=None, encoding=None, execute_filemode=None, last_commit_id=None, start_branch=None):
    """
    Updates a file in a GitLab repository with new content.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project.
        file_path (str): URL-encoded full path to the file to be updated.
        content (str): The new content of the file.
        branch (str): Name of the branch where the file will be updated.
        commit_message (str): The commit message.
        author_name (str, optional): The commit author's name.
        author_email (str, optional): The commit author's email address.
        encoding (str, optional): Change encoding to 'base64'. Default is 'text'.
        execute_filemode (bool, optional): Enables or disables the execute flag on the file.
        last_commit_id (str, optional): Last known file commit ID.
        start_branch (str, optional): Name of the base branch to create the new branch from.
    
    Returns:
        Returns information about the updated file including its path and the branch where it was modified."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{project_id}/repository/files/{quote(file_path, safe='')}"
    
    data = {
        'branch': branch,
        'content': content,
        'commit_message': commit_message
    }
    
    # Add optional parameters if provided
    if author_name:
        data['author_name'] = author_name
    if author_email:
        data['author_email'] = author_email
    if encoding:
        data['encoding'] = encoding
    if execute_filemode is not None:
        data['execute_filemode'] = execute_filemode
    if last_commit_id:
        data['last_commit_id'] = last_commit_id
    if start_branch:
        data['start_branch'] = start_branch
    
    response = requests.put(url, headers=headers, data=json.dumps(data))
    return response

if __name__ == '__main__':
    r = update_repository_file(
        project_id=183,
        file_path="README.md",
        content="# Updated Project\n\nThis file has been updated through the GitLab API.",
        branch="main",
        commit_message="Update README.md through API",
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