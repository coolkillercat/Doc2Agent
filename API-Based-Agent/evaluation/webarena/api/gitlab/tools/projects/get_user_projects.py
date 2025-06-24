import requests, json
from urllib.parse import quote



def get_user_projects(user_id: str, archived: bool = None, membership: bool = None, min_access_level: int = None, order_by: str = 'created_at', owned: bool = None, search: str = None, simple: bool = None, sort: str = 'desc', starred: bool = None, statistics: bool = None, visibility: str = None, with_programming_language: str = None, with_issues_enabled: bool = None, with_merge_requests_enabled: bool = None):
    """
    Retrieves a list of projects owned by a specific GitLab user, with flexible filtering options to narrow down results based on project attributes like visibility, activity status, and features.
    
    Args:
        user_id (str): The ID or username of the user
        archived (bool, optional): Limit by archived status
        membership (bool, optional): Limit by projects that the current user is a member of
        min_access_level (int, optional): Limit by current user minimal role (access_level)
        order_by (str, optional): Return projects ordered by specified field. Default is 'created_at'
        owned (bool, optional): Limit by projects explicitly owned by the current user
        search (str, optional): Return list of projects matching the search criteria
        simple (bool, optional): Return only limited fields for each project
        sort (str, optional): Return projects sorted in 'asc' or 'desc' order. Default is 'desc'
        starred (bool, optional): Limit by projects starred by the current user
        statistics (bool, optional): Include project statistics
        visibility (str, optional): Limit by visibility 'public', 'internal', or 'private'
        with_programming_language (str, optional): Limit by projects which use the given programming language
        with_issues_enabled (bool, optional): Limit by enabled issues feature
        with_merge_requests_enabled (bool, optional): Limit by enabled merge requests feature
        
    Returns:
        Returns a list of projects owned by a specific GitLab user with comprehensive details including metadata, settings, permissions, and statistics."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"/users/{quote(str(user_id))}/projects"
    
    params = {
        'archived': archived,
        'membership': membership,
        'min_access_level': min_access_level,
        'order_by': order_by,
        'owned': owned,
        'search': search,
        'simple': simple,
        'sort': sort,
        'starred': starred,
        'statistics': statistics,
        'visibility': visibility,
        'with_programming_language': with_programming_language,
        'with_issues_enabled': with_issues_enabled,
        'with_merge_requests_enabled': with_merge_requests_enabled
    }
    
    # Remove None values
    params = {k: v for k, v in params.items() if v is not None}
    
    response = requests.get(base_url + endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_user_projects(user_id="byteblaze", statistics=True, order_by="updated_at")
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