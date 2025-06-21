import requests, json
from urllib.parse import quote

def get_group_audit_events(group_id: str, created_after: str = None, created_before: str = None, author_id: int = None, author_name: str = None, entity_type: str = None, entity_id: int = None, action: str = None, sort: str = 'created_desc', page: int = 1, per_page: int = 20):
    """
    Retrieves audit events for a specified group with optional filtering parameters. Allows organizations to monitor and review security-relevant actions taken within their GitLab group.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        created_after (str, optional): Return audit events created after the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)
        created_before (str, optional): Return audit events created before the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)
        author_id (int, optional): Return audit events for the specified author ID
        author_name (str, optional): Return audit events for the specified author name
        entity_type (str, optional): Return audit events for the specified entity type
        entity_id (int, optional): Return audit events for the specified entity ID
        action (str, optional): Return audit events for the specified action
        sort (str, optional): Sort audit events by created_at. Default is created_desc (descending)
        page (int, optional): Page number of the results to retrieve. Default is 1
        per_page (int, optional): Number of results per page. Default is 20
        
    Returns:
        requests.Response: The API response containing group audit events
        
    Example:
        >>> get_group_audit_events(group_id='183')
        >>> get_group_audit_events(group_id='183', author_id=2330, created_after='2025-06-12T02:26:05.054Z')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{quote(str(group_id), safe='')}/audit_events"
    
    params = {
        'page': page,
        'per_page': per_page,
        'sort': sort
    }
    
    # Add optional parameters if they are provided
    if created_after:
        params['created_after'] = created_after
    if created_before:
        params['created_before'] = created_before
    if author_id:
        params['author_id'] = author_id
    if author_name:
        params['author_name'] = author_name
    if entity_type:
        params['entity_type'] = entity_type
    if entity_id:
        params['entity_id'] = entity_id
    if action:
        params['action'] = action
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_group_audit_events(group_id='183')
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