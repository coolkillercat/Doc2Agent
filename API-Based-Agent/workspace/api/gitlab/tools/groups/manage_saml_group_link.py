import requests, json
from urllib.parse import quote

def manage_saml_group_link(group_id: int, action: str, saml_group_name: str = None, access_level: int = None, member_role_id: int = None):
    """
    Manages SAML group links for GitLab groups. Allows listing all links, retrieving a specific link, adding a new link, or deleting an existing link based on the action parameter.
    
    Args:
        group_id (int): ID of the GitLab group
        action (str): Action to perform ('list', 'get', 'add', or 'delete')
        saml_group_name (str, optional): Name of the SAML group (required for 'get', 'add', and 'delete' actions)
        access_level (int, optional): Role access level (required for 'add' action)
        member_role_id (int, optional): Member Role ID (optional for 'add' action)
        
    Returns:
        Response object from the API call
        
    Examples:
        # List all SAML group links for a group
        manage_saml_group_link(group_id=183, action="list")
        
        # Get a specific SAML group link
        manage_saml_group_link(group_id=183, action="get", saml_group_name="saml-group-1")
        
        # Add a new SAML group link
        manage_saml_group_link(group_id=183, action="add", saml_group_name="saml-group-1", access_level=10, member_role_id=12)
        
        # Delete a SAML group link
        manage_saml_group_link(group_id=183, action="delete", saml_group_name="saml-group-1")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    if action == "list":
        url = f"{base_url}/groups/{group_id}/saml_group_links"
        return requests.get(url, headers=headers)
    
    elif action == "get":
        if not saml_group_name:
            raise ValueError("saml_group_name is required for 'get' action")
        encoded_saml_group_name = quote(saml_group_name, safe='')
        url = f"{base_url}/groups/{group_id}/saml_group_links/{encoded_saml_group_name}"
        return requests.get(url, headers=headers)
    
    elif action == "add":
        if not saml_group_name or access_level is None:
            raise ValueError("saml_group_name and access_level are required for 'add' action")
        url = f"{base_url}/groups/{group_id}/saml_group_links"
        payload = {
            "saml_group_name": saml_group_name,
            "access_level": access_level
        }
        if member_role_id is not None:
            payload["member_role_id"] = member_role_id
        return requests.post(url, headers=headers, json=payload)
    
    elif action == "delete":
        if not saml_group_name:
            raise ValueError("saml_group_name is required for 'delete' action")
        encoded_saml_group_name = quote(saml_group_name, safe='')
        url = f"{base_url}/groups/{group_id}/saml_group_links/{encoded_saml_group_name}"
        return requests.delete(url, headers=headers)
    
    else:
        raise ValueError("Action must be one of: 'list', 'get', 'add', 'delete'")

if __name__ == '__main__':
    r = manage_saml_group_link(group_id=183, action="list")
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