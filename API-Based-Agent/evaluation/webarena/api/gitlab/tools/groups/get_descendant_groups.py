import requests, json
from urllib.parse import quote


def get_descendant_groups(group_id: str, search: str = None, order_by: str = 'name', sort: str = 'asc', 
                          all_available: bool = None, statistics: bool = False, with_custom_attributes: bool = False, 
                          owned: bool = False, min_access_level: int = None, skip_groups: list = None):
    """
    Retrieves a list of visible descendant groups for a specified parent group. Useful for organizational hierarchy mapping, finding subgroups, and group structure analysis.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        search (str, optional): Return groups matching the search criteria
        order_by (str, optional): Order groups by 'name', 'path', or 'id'. Default is 'name'
        sort (str, optional): Order groups in 'asc' or 'desc' order. Default is 'asc'
        all_available (bool, optional): Show all groups you have access to
        statistics (bool, optional): Include group statistics (administrators only)
        with_custom_attributes (bool, optional): Include custom attributes in response (administrators only)
        owned (bool, optional): Limit to groups explicitly owned by the current user
        min_access_level (int, optional): Limit to groups where current user has at least this role
        skip_groups (list, optional): Skip the group IDs passed
        
    Returns:
        Response: The API response containing the list of descendant groups
        
    Example:
        >>> get_descendant_groups(group_id='183')
        >>> get_descendant_groups(group_id='183', search='test', order_by='path', sort='desc')
        >>> get_descendant_groups(group_id='183', all_available=True, statistics=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{quote(str(group_id), safe='')}/descendant_groups"
    
    params = {}
    if search is not None:
        params['search'] = search
    if order_by:
        params['order_by'] = order_by
    if sort:
        params['sort'] = sort
    if all_available is not None:
        params['all_available'] = all_available
    if statistics:
        params['statistics'] = statistics
    if with_custom_attributes:
        params['with_custom_attributes'] = with_custom_attributes
    if owned:
        params['owned'] = owned
    if min_access_level is not None:
        params['min_access_level'] = min_access_level
    if skip_groups:
        params['skip_groups'] = skip_groups
    
    return requests.get(url, headers=headers, params=params)

if __name__ == '__main__':
    r = get_descendant_groups(group_id='183')
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