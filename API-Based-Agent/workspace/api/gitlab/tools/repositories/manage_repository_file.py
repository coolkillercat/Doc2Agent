import requests, json
from urllib.parse import quote



def manage_repository_file(project_id: str, file_path: str, branch: str = 'main', operation: str = 'get', content: str = None, commit_message: str = None, encoding: str = 'text', author_email: str = None, author_name: str = None):
    """
    Manages repository files by performing operations like get, create, update, or delete on a specific file in a GitLab project repository.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        file_path (str): The path to the file. Must be URL-encoded.
        branch (str, optional): The name of the branch. Defaults to 'main'.
        operation (str, optional): The operation to perform - 'get', 'create', 'update', or 'delete'. Defaults to 'get'.
        content (str, optional): The content of the file for create/update operations. Defaults to None.
        commit_message (str, optional): The commit message. Required for create/update/delete. Defaults to None.
        encoding (str, optional): The encoding of the file. Defaults to 'text'.
        author_email (str, optional): The email of the author. Defaults to None.
        author_name (str, optional): The name of the author. Defaults to None.
        
    Returns:
        Returns file metadata and content from a GitLab repository, including file name, path, size, encoding, and commit information."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # URL encode the file path
    encoded_file_path = quote(file_path, safe='')
    
    if operation == 'get':
        url = f"{base_url}/projects/{project_id}/repository/files/{encoded_file_path}?ref={branch}"
        return requests.get(url, headers=headers)
    
    elif operation in ['create', 'update', 'delete']:
        url = f"{base_url}/projects/{project_id}/repository/files/{encoded_file_path}"
        
        data = {
            'branch': branch,
            'commit_message': commit_message or f"{operation.capitalize()} file {file_path}"
        }
        
        if operation in ['create', 'update']:
            data['content'] = content
            data['encoding'] = encoding
        
        if author_email:
            data['author_email'] = author_email
        
        if author_name:
            data['author_name'] = author_name
        
        if operation == 'create':
            return requests.post(url, headers=headers, json=data)
        elif operation == 'update':
            return requests.put(url, headers=headers, json=data)
        elif operation == 'delete':
            return requests.delete(url, headers=headers, json=data)
    
    else:
        raise ValueError(f"Invalid operation: {operation}. Choose 'get', 'create', 'update', or 'delete'.")

if __name__ == '__main__':
    r = manage_repository_file(project_id=183, file_path='README.md', branch='main', operation='get')
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