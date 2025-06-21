import requests
from urllib.parse import quote
import os
import io

def upload_file_to_project(project_id: str, file_path: str, file_content: str = None, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token: str = "glpat-qvQ-N6mN_tAddXb2WWdi") -> dict:
    """
    Uploads a file to a specified GitLab project for use in issue descriptions, merge requests, or comments.
    
    Args:
        project_id (str): The ID of the project where the file will be uploaded
        file_path (str): The local path to the file to be uploaded or the name to use for the file
        file_content (str, optional): The content to upload if file_path doesn't exist
        base_url (str, optional): The base URL of the GitLab API
        token (str, optional): The private token for authentication
        
    Returns:
        Returns file upload details including the URL, full path, and Markdown representation for use in GitLab issues, merge requests, or comments.
    Example:
        >>> upload_file_to_project("183", "test_file.txt", "This is test content")
        {
            "alt": "test_file",
            "url": "/uploads/66dbcd21ec5d24ed6ea225176098d52b/test_file.txt",
            "full_path": "/namespace1/project1/uploads/66dbcd21ec5d24ed6ea225176098d52b/test_file.txt",
            "markdown": "![test_file](/uploads/66dbcd21ec5d24ed6ea225176098d52b/test_file.txt)"
        }
    """
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/uploads"
    headers = {'PRIVATE-TOKEN': token}
    
    if file_content is not None or not os.path.exists(file_path):
        # If file doesn't exist or content is provided, use the content directly
        content = file_content if file_content is not None else f"Test content for {file_path}"
        file_obj = io.BytesIO(content.encode('utf-8'))
        filename = os.path.basename(file_path)
        files = {'file': (filename, file_obj)}
        response = requests.post(url, headers=headers, files=files)
    else:
        # Use the actual file if it exists
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, headers=headers, files=files)
    
    return response

if __name__ == '__main__':
    r = upload_file_to_project(project_id=183, file_path="test_file.txt", file_content="This is a test file content")
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