import requests, json
from urllib.parse import quote



def get_raw_file(project_id: str, file_path: str, ref: str = 'HEAD', lfs: bool = False):
    """
    Retrieves the raw content of a file from a GitLab repository. Useful for viewing source code, documentation, or other file contents directly.
    
    Args:
        project_id (str): The ID of the project.
        file_path (str): Path to the file in the repository.
        ref (str, optional): The name of branch, tag or commit. Defaults to 'HEAD'.
        lfs (bool, optional): Whether to return Git LFS file contents. Defaults to False.
    
    Returns:
        Returns the raw content of a file from a GitLab repository as plain text."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # URL encode the file path
    encoded_file_path = quote(file_path, safe='')
    
    # Construct the URL
    url = f"{base_url}/projects/{project_id}/repository/files/{encoded_file_path}/raw"
    
    # Add query parameters
    params = {
        'ref': ref
    }
    
    if lfs:
        params['lfs'] = 'true'
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_raw_file(project_id=183, file_path="README.md", ref="main")
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