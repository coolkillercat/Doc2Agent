import requests, json
from urllib.parse import quote

def get_project_changelogs(project_id: str, date_from: str = None, date_to: str = None, version: str = None, limit: int = 20) -> dict:
    """
    Retrieves changelogs for a specific project, allowing users to track changes and updates over time. 
    Supports filtering by date range and specific version.
    
    Args:
        project_id (str): The ID of the project.
        date_from (str, optional): Start date for filtering changelogs (format: YYYY-MM-DD).
        date_to (str, optional): End date for filtering changelogs (format: YYYY-MM-DD).
        version (str, optional): Filter changelogs by specific version.
        limit (int, optional): Maximum number of changelog entries to return. Default is 20.
        
    Returns:
        dict: Response object containing the project changelogs.
        
    Example:
        >>> get_project_changelogs(project_id='183', date_from='2023-01-01', limit=10)
        <Response [200]>
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/changelogs"
    
    params = {'limit': limit}
    
    if date_from:
        params['from'] = date_from
    
    if date_to:
        params['to'] = date_to
    
    if version:
        params['version'] = version
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_changelogs(project_id='183', date_from='2023-01-01', limit=10)
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