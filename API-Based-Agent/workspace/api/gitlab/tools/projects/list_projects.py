import requests, json
from urllib.parse import quote



def list_projects(archived: bool = None, membership: bool = None, owned: bool = None, starred: bool = None, visibility: str = None, order_by: str = 'created_at', sort: str = 'desc', search: str = None, simple: bool = None, topics: str = None, min_access_level: int = None, with_issues_enabled: bool = None, with_merge_requests_enabled: bool = None, statistics: bool = None, with_programming_language: str = None):
    """
    Retrieves a list of GitLab projects matching specified criteria. This tool helps users find projects they have access to, filter by various attributes, and control the data returned in the response.
    
    Args:
        archived (bool, optional): Limit by archived status.
        membership (bool, optional): Limit by projects that the current user is a member of.
        owned (bool, optional): Limit by projects explicitly owned by the current user.
        starred (bool, optional): Limit by projects starred by the current user.
        visibility (str, optional): Limit by visibility 'public', 'internal', or 'private'.
        order_by (str, optional): Return projects ordered by specific field. Default is 'created_at'.
        sort (str, optional): Return projects sorted in 'asc' or 'desc' order. Default is 'desc'.
        search (str, optional): Return list of projects matching the search criteria.
        simple (bool, optional): Return only limited fields for each project.
        topics (str, optional): Comma-separated topic names to filter projects by.
        min_access_level (int, optional): Limit by current user minimal role access level.
        with_issues_enabled (bool, optional): Limit by enabled issues feature.
        with_merge_requests_enabled (bool, optional): Limit by enabled merge requests feature.
        statistics (bool, optional): Include project statistics.
        with_programming_language (str, optional): Limit by projects which use the given programming language.
        
    Returns:
        Returns a list of visible GitLab projects with comprehensive details including metadata, settings, permissions, and statistics."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects"
    
    params = {}
    if archived is not None:
        params['archived'] = archived
    if membership is not None:
        params['membership'] = membership
    if owned is not None:
        params['owned'] = owned
    if starred is not None:
        params['starred'] = starred
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
    if topics is not None:
        params['topic'] = topics
    if min_access_level is not None:
        params['min_access_level'] = min_access_level
    if with_issues_enabled is not None:
        params['with_issues_enabled'] = with_issues_enabled
    if with_merge_requests_enabled is not None:
        params['with_merge_requests_enabled'] = with_merge_requests_enabled
    if statistics is not None:
        params['statistics'] = statistics
    if with_programming_language is not None:
        params['with_programming_language'] = with_programming_language
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_projects(membership=True, order_by='name', statistics=True)
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