import requests, json
from urllib.parse import quote



def list_users(search: str = None, username: str = None, active: bool = None, external: bool = None, exclude_external: bool = None, blocked: bool = None, created_after: str = None, created_before: str = None, exclude_internal: bool = None, without_project_bots: bool = None, order_by: str = None, sort: str = 'desc', two_factor: str = None, without_projects: bool = None, admins: bool = None, auditors: bool = None, extern_uid: str = None, provider: str = None, saml_provider_id: int = None, skip_ldap: bool = None, page: int = 1, per_page: int = 20, with_custom_attributes: bool = None):
    """
    Retrieves a list of GitLab users with comprehensive filtering options including by username, activity status, creation date, and user type. Supports pagination and sorting to efficiently manage large user directories.
    
    Args:
        search (str, optional): Search for users by name, username, or email.
        username (str, optional): Get a single user with a specific username.
        active (bool, optional): Filter only active users.
        external (bool, optional): Filter only external users.
        exclude_external (bool, optional): Filter only non-external users.
        blocked (bool, optional): Filter only blocked users.
        created_after (str, optional): Returns users created after specified time (DateTime format).
        created_before (str, optional): Returns users created before specified time (DateTime format).
        exclude_internal (bool, optional): Filters only non-internal users.
        without_project_bots (bool, optional): Filters users without project bots.
        order_by (str, optional): Return users ordered by id, name, username, created_at, or updated_at.
        sort (str, optional): Return users sorted in asc or desc order. Default is desc.
        two_factor (str, optional): Filter users by Two-factor authentication (enabled/disabled).
        without_projects (bool, optional): Filter users without projects.
        admins (bool, optional): Return only administrators.
        auditors (bool, optional): Return only auditor users (Premium/Ultimate only).
        extern_uid (str, optional): Get users with a specific external authentication provider UID.
        provider (str, optional): The external provider.
        saml_provider_id (int, optional): Return only users created by the specified SAML provider ID.
        skip_ldap (bool, optional): Skip LDAP users (Premium/Ultimate only).
        page (int, optional): Page number for pagination. Default is 1.
        per_page (int, optional): Number of items per page. Default is 20.
        with_custom_attributes (bool, optional): Include custom attributes in the response.
        
    Returns:
        Returns a list of GitLab users with their basic profile information including ID, username, name, state, and URLs."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/users"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    params = {}
    
    # Add all parameters that are not None
    if search is not None:
        params['search'] = search
    if username is not None:
        params['username'] = username
    if active is not None:
        params['active'] = active
    if external is not None:
        params['external'] = external
    if exclude_external is not None:
        params['exclude_external'] = exclude_external
    if blocked is not None:
        params['blocked'] = blocked
    if created_after is not None:
        params['created_after'] = created_after
    if created_before is not None:
        params['created_before'] = created_before
    if exclude_internal is not None:
        params['exclude_internal'] = exclude_internal
    if without_project_bots is not None:
        params['without_project_bots'] = without_project_bots
    if order_by is not None:
        params['order_by'] = order_by
    if sort is not None:
        params['sort'] = sort
    if two_factor is not None:
        params['two_factor'] = two_factor
    if without_projects is not None:
        params['without_projects'] = without_projects
    if admins is not None:
        params['admins'] = admins
    if auditors is not None:
        params['auditors'] = auditors
    if extern_uid is not None:
        params['extern_uid'] = extern_uid
    if provider is not None:
        params['provider'] = provider
    if saml_provider_id is not None:
        params['saml_provider_id'] = saml_provider_id
    if skip_ldap is not None:
        params['skip_ldap'] = skip_ldap
    if with_custom_attributes is not None:
        params['with_custom_attributes'] = with_custom_attributes
    
    # Add pagination parameters
    params['page'] = page
    params['per_page'] = per_page
    
    response = requests.get(endpoint, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = list_users(username="byteblaze", per_page=10)
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