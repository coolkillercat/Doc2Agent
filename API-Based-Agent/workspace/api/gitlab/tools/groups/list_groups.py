import requests, json
from urllib.parse import quote

def list_groups(skip_groups: list = None, all_available: bool = None, search: str = None, order_by: str = None, sort: str = None, statistics: bool = False, visibility: str = None, with_custom_attributes: bool = False, owned: bool = False, min_access_level: int = None, top_level_only: bool = False, repository_storage: str = None):
    """
    Retrieves a list of visible GitLab groups based on specified filters. Allows searching, sorting, and filtering groups by various criteria such as visibility, ownership, and access level.
    
    Args:
        skip_groups (list, optional): List of group IDs to skip.
        all_available (bool, optional): Show all groups the user has access to.
        search (str, optional): Search criteria to filter groups.
        order_by (str, optional): Order groups by 'name', 'path', 'id', or 'similarity'.
        sort (str, optional): Sort order, 'asc' or 'desc'.
        statistics (bool, optional): Include group statistics.
        visibility (str, optional): Filter by visibility ('public', 'internal', or 'private').
        with_custom_attributes (bool, optional): Include custom attributes in response.
        owned (bool, optional): Limit to groups explicitly owned by the current user.
        min_access_level (int, optional): Limit to groups where user has at least this role.
        top_level_only (bool, optional): Limit to top level groups, excluding subgroups.
        repository_storage (str, optional): Filter by repository storage used by the group.
        
    Returns:
        Returns a list of visible GitLab groups with optional filtering by criteria such as visibility, ownership, and access level."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/groups"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    params = {}
    
    if skip_groups:
        params['skip_groups'] = skip_groups
    if all_available is not None:
        params['all_available'] = all_available
    if search:
        params['search'] = search
    if order_by:
        params['order_by'] = order_by
    if sort:
        params['sort'] = sort
    if statistics:
        params['statistics'] = statistics
    if visibility:
        params['visibility'] = visibility
    if with_custom_attributes:
        params['with_custom_attributes'] = with_custom_attributes
    if owned:
        params['owned'] = owned
    if min_access_level is not None:
        params['min_access_level'] = min_access_level
    if top_level_only:
        params['top_level_only'] = top_level_only
    if repository_storage:
        params['repository_storage'] = repository_storage
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_groups(statistics=True, visibility="public", order_by="name", sort="asc")
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