import requests
from urllib.parse import quote


def sync_group_with_ldap(group_id: str, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", 
                         token: str = "glpat-qvQ-N6mN_tAddXb2WWdi"):
    """
    Synchronizes a GitLab group with its linked LDAP group. This ensures that group membership and permissions stay consistent with the external LDAP directory.
    
    Args:
        group_id (str): The ID or path of the user group to synchronize with LDAP
        base_url (str, optional): The base URL of the GitLab API
        token (str, optional): The private token for authentication
        
    Returns:
        requests.Response: The response from the API
        
    Example:
        >>> response = sync_group_with_ldap('2597')
        >>> response = sync_group_with_ldap('Test Group')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    
    url = f"{base_url}/groups/{quote(str(group_id), safe='')}/ldap_sync"
    response = requests.post(url, headers=headers)
    
    return response


if __name__ == '__main__':
    r = sync_group_with_ldap(group_id='183')
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