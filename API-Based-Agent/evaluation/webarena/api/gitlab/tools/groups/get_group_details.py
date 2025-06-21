import requests, json
from urllib.parse import quote

def get_group_details(group_id: int, with_projects: bool = None, with_custom_attributes: bool = None, 
                     with_shared_projects: bool = None, with_shared_runners_setting: bool = None) -> dict:
    """
    Retrieves comprehensive information about a GitLab group, including name, description, visibility settings, and other attributes.
    This allows users to view group configuration details for management or reporting purposes.
    
    Args:
        group_id (int): The ID of the group to retrieve details for.
        with_projects (bool, optional): Include details of projects in the group.
        with_custom_attributes (bool, optional): Include custom attributes in the response.
        with_shared_projects (bool, optional): Include shared projects in the response.
        with_shared_runners_setting (bool, optional): Include shared runners setting in the response.
        
    Returns:
        dict: The JSON response containing group details.
        
    Example:
        >>> get_group_details(183)
        >>> get_group_details(183, with_projects=True)
        >>> get_group_details(183, with_custom_attributes=True, with_shared_projects=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{group_id}"
    
    params = {}
    if with_projects is not None:
        params['with_projects'] = with_projects
    if with_custom_attributes is not None:
        params['with_custom_attributes'] = with_custom_attributes
    if with_shared_projects is not None:
        params['with_shared_projects'] = with_shared_projects
    if with_shared_runners_setting is not None:
        params['with_shared_runners_setting'] = with_shared_runners_setting
    
    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else response

if __name__ == '__main__':
    r = get_group_details(group_id=183)
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