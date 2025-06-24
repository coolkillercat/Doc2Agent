import requests, json
from urllib.parse import quote



def list_project_forks(project_id: int or str, archived: bool = None, membership: bool = None, min_access_level: int = None, order_by: str = None, owned: bool = None, search: str = None, simple: bool = None, sort: str = None, starred: bool = None, statistics: bool = None, updated_after: str = None, updated_before: str = None, visibility: str = None, with_custom_attributes: bool = None, with_issues_enabled: bool = None, with_merge_requests_enabled: bool = None):
    """
    Retrieves a list of fork projects derived from a specified source project. This function helps users discover and track project forks, supporting filtering by various attributes like visibility, activity dates, and features enabled.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        archived (bool, optional): Limit by archived status
        membership (bool, optional): Limit by projects that the current user is a member of
        min_access_level (int, optional): Limit by current user minimal role
        order_by (str, optional): Return projects ordered by specified field
        owned (bool, optional): Limit by projects explicitly owned by the current user
        search (str, optional): Return list of projects matching the search criteria
        simple (bool, optional): Return only limited fields for each project
        sort (str, optional): Return projects sorted in 'asc' or 'desc' order
        starred (bool, optional): Limit by projects starred by the current user
        statistics (bool, optional): Include project statistics
        updated_after (str, optional): Limit results to projects last updated after the specified time
        updated_before (str, optional): Limit results to projects last updated before the specified time
        visibility (str, optional): Limit by visibility 'public', 'internal', or 'private'
        with_custom_attributes (bool, optional): Include custom attributes in response
        with_issues_enabled (bool, optional): Limit by enabled issues feature
        with_merge_requests_enabled (bool, optional): Limit by enabled merge requests feature
    
    Returns:
        Returns a list of fork projects derived from a specified source project with comprehensive details including metadata, settings, permissions, and parent project information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct URL
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/forks"
    
    # Build query parameters
    params = {}
    if archived is not None:
        params['archived'] = archived
    if membership is not None:
        params['membership'] = membership
    if min_access_level is not None:
        params['min_access_level'] = min_access_level
    if order_by is not None:
        params['order_by'] = order_by
    if owned is not None:
        params['owned'] = owned
    if search is not None:
        params['search'] = search
    if simple is not None:
        params['simple'] = simple
    if sort is not None:
        params['sort'] = sort
    if starred is not None:
        params['starred'] = starred
    if statistics is not None:
        params['statistics'] = statistics
    if updated_after is not None:
        params['updated_after'] = updated_after
    if updated_before is not None:
        params['updated_before'] = updated_before
    if visibility is not None:
        params['visibility'] = visibility
    if with_custom_attributes is not None:
        params['with_custom_attributes'] = with_custom_attributes
    if with_issues_enabled is not None:
        params['with_issues_enabled'] = with_issues_enabled
    if with_merge_requests_enabled is not None:
        params['with_merge_requests_enabled'] = with_merge_requests_enabled
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_project_forks(project_id=183)
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