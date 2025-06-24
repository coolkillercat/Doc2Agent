import requests, json
from urllib.parse import quote

def list_group_users(group_id, include_saml_users=False, include_service_accounts=False, search=None):
    """
    Retrieves a list of users associated with a specific group, including options to filter for SAML users or service accounts.
    
    This endpoint requires Owner role in the group and returns users that are related to a top-level group
    regardless of their current membership.
    
    Args:
        group_id (int or str): ID or URL-encoded path of the group
        include_saml_users (bool): Whether to include users with a SAML identity
        include_service_accounts (bool): Whether to include service account users
        search (str, optional): Search users by name, email, username
        
    Returns:
        Response object from the API request
        
    Examples:
        >>> list_group_users(183, include_saml_users=True)
        >>> list_group_users(183, include_service_accounts=True, search="byteblaze")
        >>> list_group_users(183, include_saml_users=True, include_service_accounts=True)
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # Either include_saml_users or include_service_accounts must be True
    if not include_saml_users and not include_service_accounts:
        include_saml_users = True  # Default to True if both are False
    
    # Construct the URL
    endpoint = f"{base_url}/groups/{quote(str(group_id), safe='')}/users"
    
    # Build query parameters
    params = {
        'include_saml_users': str(include_saml_users).lower(),
        'include_service_accounts': str(include_service_accounts).lower(),
    }
    
    # Add search parameter if provided
    if search:
        params['search'] = search
    
    # Make the request
    response = requests.get(endpoint, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = list_group_users(group_id=183, include_saml_users=True, include_service_accounts=True)
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