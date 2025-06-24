import requests, json
from urllib.parse import quote



def get_file_blame(project_id: str, file_path: str, ref: str, range_start: int = None, range_end: int = None):
    """
    Retrieves blame information for a file in a repository, showing which commits and authors are responsible for specific lines of code. Optionally allows specifying a line range to limit the blame information.

    Args:
        project_id (str): The ID or URL-encoded path of the project
        file_path (str): Path to the file to get blame for
        ref (str): The name of branch, tag or commit
        range_start (int, optional): The first line of the range to blame
        range_end (int, optional): The last line of the range to blame

    Returns:
        Returns blame information for a file showing which commits and authors are responsible for specific lines of code."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_file_path = quote(file_path, safe='')
    url = f"{base_url}/projects/{project_id}/repository/files/{encoded_file_path}/blame"
    
    params = {'ref': ref}
    
    if range_start is not None and range_end is not None:
        params['range[start]'] = range_start
        params['range[end]'] = range_end
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_file_blame(project_id=183, file_path="README.md", ref="main", range_start=1, range_end=10)
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