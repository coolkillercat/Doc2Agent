import requests, json
from urllib.parse import quote

def get_group_shared_projects(group_id, archived=None, visibility=None, order_by=None, sort=None, search=None, simple=None, starred=None, with_issues_enabled=None, with_merge_requests_enabled=None, min_access_level=None, with_custom_attributes=None):
    """
    Retrieves a list of projects shared with a specific group, allowing filtering by various criteria such as visibility, archived status, and features enabled.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group owned by the authenticated user
        archived (bool, optional): Limit by archived status
        visibility (str, optional): Limit by visibility 'public', 'internal', or 'private'
        order_by (str, optional): Return projects ordered by 'id', 'name', 'path', 'created_at', 'updated_at', 'star_count' or 'last_activity_at' fields. Default is 'created_at'
        sort (str, optional): Return projects sorted in 'asc' or 'desc' order. Default is 'desc'
        search (str, optional): Return list of authorized projects matching the search criteria
        simple (bool, optional): Return only limited fields for each project
        starred (bool, optional): Limit by projects starred by the current user
        with_issues_enabled (bool, optional): Limit by projects with issues feature enabled. Default is False
        with_merge_requests_enabled (bool, optional): Limit by projects with merge requests feature enabled. Default is False
        min_access_level (int, optional): Limit to projects where current user has at least this role
        with_custom_attributes (bool, optional): Include custom attributes in response (administrators only)
    
    Returns:
        Response: The API response containing the list of shared projects
        
    Example:
        >>> response = get_group_shared_projects(28, visibility="public", order_by="name", sort="asc")
        >>> projects = response.json()
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Prepare the endpoint URL with the group ID
    endpoint = f"{base_url}/groups/{quote(str(group_id))}/projects/shared"
    
    # Build the parameters dictionary, including only non-None values
    params = {}
    if archived is not None:
        params['archived'] = archived
    if visibility is not None:
        params['visibility'] = visibility
    if order_by is not None:
        params['order_by'] = order_by
    if sort is not None:
        params['sort'] = sort
    if search is not None:
        params['search'] = search
    if simple is not None:
        params['simple'] = simple
    if starred is not None:
        params['starred'] = starred
    if with_issues_enabled is not None:
        params['with_issues_enabled'] = with_issues_enabled
    if with_merge_requests_enabled is not None:
        params['with_merge_requests_enabled'] = with_merge_requests_enabled
    if min_access_level is not None:
        params['min_access_level'] = min_access_level
    if with_custom_attributes is not None:
        params['with_custom_attributes'] = with_custom_attributes
    
    # Make the GET request
    response = requests.get(endpoint, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_group_shared_projects(group_id=28, visibility="public", order_by="name", sort="asc")
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