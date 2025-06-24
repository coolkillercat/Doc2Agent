import requests, json
from urllib.parse import quote

def manage_ldap_group_links(group_id: str, action: str, provider: str = None, cn: str = None, filter: str = None, group_access: int = None):
    """
    A comprehensive tool for managing LDAP group links in GitLab groups. Allows listing, adding, and deleting LDAP group links using CN or filter criteria.
    
    Args:
        group_id (str): The ID or URL-encoded path of the group
        action (str): The action to perform - 'list', 'add', or 'delete'
        provider (str, optional): LDAP provider for the LDAP group link, required for 'add' and 'delete' actions
        cn (str, optional): The CN of an LDAP group
        filter (str, optional): The LDAP filter for the group
        group_access (int, optional): Role (access_level) for members of the LDAP group, required for 'add' action
        
    Returns:
        requests.Response: The API response
        
    Examples:
        # List LDAP group links
        manage_ldap_group_links(group_id='183', action='list')
        
        # Add LDAP group link with CN
        manage_ldap_group_links(group_id='183', action='add', provider='ldapmain', cn='developers', group_access=30)
        
        # Add LDAP group link with filter
        manage_ldap_group_links(group_id='183', action='add', provider='ldapmain', filter='(memberOf=cn=developers,ou=groups,dc=example,dc=com)', group_access=30)
        
        # Delete LDAP group link with CN
        manage_ldap_group_links(group_id='183', action='delete', provider='ldapmain', cn='developers')
        
        # Delete LDAP group link with filter
        manage_ldap_group_links(group_id='183', action='delete', provider='ldapmain', filter='(memberOf=cn=developers,ou=groups,dc=example,dc=com)')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_group_id = quote(str(group_id), safe='')
    
    if action == 'list':
        url = f"{base_url}/groups/{encoded_group_id}/ldap_group_links"
        return requests.get(url, headers=headers)
    
    elif action == 'add':
        if not provider or group_access is None:
            raise ValueError("Provider and group_access are required for adding LDAP group links")
        
        if (cn and filter) or (not cn and not filter):
            raise ValueError("Provide either cn or filter, but not both")
        
        url = f"{base_url}/groups/{encoded_group_id}/ldap_group_links"
        payload = {
            'provider': provider,
            'group_access': group_access
        }
        
        if cn:
            payload['cn'] = cn
        elif filter:
            payload['filter'] = filter
            
        return requests.post(url, headers=headers, json=payload)
    
    elif action == 'delete':
        if not provider:
            raise ValueError("Provider is required for deleting LDAP group links")
            
        if (cn and filter) or (not cn and not filter):
            raise ValueError("Provide either cn or filter, but not both")
        
        url = f"{base_url}/groups/{encoded_group_id}/ldap_group_links"
        payload = {'provider': provider}
        
        if cn:
            payload['cn'] = cn
        elif filter:
            payload['filter'] = filter
            
        return requests.delete(url, headers=headers, json=payload)
    
    else:
        raise ValueError("Invalid action. Use 'list', 'add', or 'delete'")

if __name__ == '__main__':
    r = manage_ldap_group_links(group_id=183, action='list')
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