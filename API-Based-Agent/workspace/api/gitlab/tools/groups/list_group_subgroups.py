import requests, json
from urllib.parse import quote


def list_group_subgroups(group_id, skip_groups=None, all_available=None, search=None, order_by=None, sort=None, statistics=None, with_custom_attributes=None, owned=None, min_access_level=None):
    """
    Retrieves visible direct subgroups for a specified parent group. Useful for navigating group hierarchies and discovering available subgroups based on various filtering criteria.
    
    Args:
        group_id (int/str): The ID or URL-encoded path of the immediate parent group
        skip_groups (list, optional): Skip the group IDs passed
        all_available (bool, optional): Show all groups you have access to
        search (str, optional): Return groups matching the search criteria
        order_by (str, optional): Order groups by name, path or id
        sort (str, optional): Order groups in asc or desc order
        statistics (bool, optional): Include group statistics (administrators only)
        with_custom_attributes (bool, optional): Include custom attributes in response (administrators only)
        owned (bool, optional): Limit to groups explicitly owned by the current user
        min_access_level (int, optional): Limit to groups where current user has at least this role
        
    Returns:
        requests.Response: The API response containing the list of subgroups
        
    Example:
        >>> response = list_group_subgroups(group_id=183)
        >>> response = list_group_subgroups(group_id=183, all_available=True, order_by='name', sort='asc')
        >>> response = list_group_subgroups(group_id='my-group', search='test', min_access_level=30)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Handle URL encoding for string paths
    if isinstance(group_id, str) and not str(group_id).isdigit():
        group_id = quote(group_id, safe='')
    
    url = f"{base_url}/groups/{group_id}/subgroups"
    
    params = {}
    if skip_groups is not None:
        params['skip_groups'] = skip_groups
    if all_available is not None:
        params['all_available'] = all_available
    if search is not None:
        params['search'] = search
    if order_by is not None:
        params['order_by'] = order_by
    if sort is not None:
        params['sort'] = sort
    if statistics is not None:
        params['statistics'] = statistics
    if with_custom_attributes is not None:
        params['with_custom_attributes'] = with_custom_attributes
    if owned is not None:
        params['owned'] = owned
    if min_access_level is not None:
        params['min_access_level'] = min_access_level
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_group_subgroups(group_id=183)
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