import requests, json
from urllib.parse import quote
from typing import Union


def get_repository_file(project_id: Union[int, str], file_path: str, ref: str = 'main', metadata_only: bool = False):
    """
    Retrieves a file from a GitLab repository, including its contents and metadata. The file content is returned Base64 encoded. Setting metadata_only to True uses a HEAD request to return only file metadata without the content.
    
    Args:
        project_id: The ID or URL-encoded path of the project
        file_path: URL encoded full path to the file
        ref: The name of branch, tag or commit
        metadata_only: If True, only file metadata will be returned without content
    
    Returns:
        Returns file information from a GitLab repository including name, path, size, encoding, and Base64-encoded content."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_file_path = quote(file_path, safe='')
    url = f"{base_url}/projects/{project_id}/repository/files/{encoded_file_path}?ref={ref}"
    
    if metadata_only:
        return requests.head(url, headers=headers)
    else:
        return requests.get(url, headers=headers)

if __name__ == '__main__':
    r = get_repository_file(project_id=183, file_path="README.md", ref="main")
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