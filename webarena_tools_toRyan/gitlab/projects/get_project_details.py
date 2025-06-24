import requests, json
from urllib.parse import quote



def get_project_details(project_id: int, include_license: bool = False, include_statistics: bool = False, include_custom_attributes: bool = False):
    """
    Retrieves detailed information about a specific project, including description, visibility, repository URLs, and other project metadata. Useful for project management and monitoring.
    
    Args:
        project_id: The ID of the project to retrieve
        include_license: Include project license data
        include_statistics: Include project statistics (requires at least Reporter role)
        include_custom_attributes: Include custom attributes in response (administrators only)
        
    Returns:
        Retrieves detailed information about a specific project, including description, visibility, repository URLs, and other project metadata."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Add query parameters if specified
    params = {}
    if include_license:
        params['license'] = True
    if include_statistics:
        params['statistics'] = True
    if include_custom_attributes:
        params['with_custom_attributes'] = True
    
    url = f"{base_url}/projects/{project_id}"
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_details(project_id=183, include_statistics=True)
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