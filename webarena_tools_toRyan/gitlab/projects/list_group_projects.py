import requests, json
from urllib.parse import quote

def list_group_projects(group_id: int or str, archived: bool = None, visibility: str = None, order_by: str = None, sort: str = None, search: str = None, simple: bool = None, owned: bool = None, starred: bool = None, topic: str = None, with_issues_enabled: bool = None, with_merge_requests_enabled: bool = None, with_shared: bool = True, include_subgroups: bool = False, min_access_level: int = None, with_custom_attributes: bool = None, with_security_reports: bool = None):
    """
    Retrieves a list of projects belonging to a specific group, with extensive filtering capabilities such as visibility, ownership, and feature enablement. Useful for project management, reporting, and group-level operations.
    
    Args:
        group_id (int or str): The ID or URL-encoded path of the group
        archived (bool, optional): Limit by archived status
        visibility (str, optional): Limit by visibility 'public', 'internal', or 'private'
        order_by (str, optional): Return projects ordered by specified field
        sort (str, optional): Return projects sorted in 'asc' or 'desc' order
        search (str, optional): Return projects matching the search criteria
        simple (bool, optional): Return only limited fields for each project
        owned (bool, optional): Limit by projects owned by the current user
        starred (bool, optional): Limit by projects starred by the current user
        topic (str, optional): Return projects matching the topic
        with_issues_enabled (bool, optional): Limit by projects with issues feature enabled
        with_merge_requests_enabled (bool, optional): Limit by projects with merge requests feature enabled
        with_shared (bool, optional): Include projects shared to this group
        include_subgroups (bool, optional): Include projects in subgroups of this group
        min_access_level (int, optional): Limit to projects where current user has at least this role
        with_custom_attributes (bool, optional): Include custom attributes in response
        with_security_reports (bool, optional): Return only projects that have security reports artifacts
    
    Returns:
        Response: HTTP response object from the API request
        
    Examples:
        >>> list_group_projects(183, visibility="public", order_by="created_at", sort="desc")
        >>> list_group_projects("primer", include_subgroups=True)
        >>> list_group_projects(183, search="test", with_issues_enabled=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # Convert group_id to URL-encoded string if it's not already a string
    if not isinstance(group_id, str):
        group_id = str(group_id)
    group_id = quote(group_id, safe='')
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{group_id}/projects"
    
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
    if owned is not None:
        params['owned'] = owned
    if starred is not None:
        params['starred'] = starred
    if topic is not None:
        params['topic'] = topic
    if with_issues_enabled is not None:
        params['with_issues_enabled'] = with_issues_enabled
    if with_merge_requests_enabled is not None:
        params['with_merge_requests_enabled'] = with_merge_requests_enabled
    if with_shared is not None:
        params['with_shared'] = with_shared
    if include_subgroups is not None:
        params['include_subgroups'] = include_subgroups
    if min_access_level is not None:
        params['min_access_level'] = min_access_level
    if with_custom_attributes is not None:
        params['with_custom_attributes'] = with_custom_attributes
    if with_security_reports is not None:
        params['with_security_reports'] = with_security_reports
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_group_projects(group_id=183, visibility="public", order_by="created_at", sort="desc")
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