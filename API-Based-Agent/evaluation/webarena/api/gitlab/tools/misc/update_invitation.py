import requests, json
from urllib.parse import quote



def update_invitation(resource_type: str, resource_id: int | str, email: str, access_level: int = 30, expires_at: str = None) -> dict:
    """
    Updates a pending invitation's access level or expiry date for a GitLab group or project. Allows modifying permissions or time limits for users who have been invited but haven't yet accepted.
    
    Args:
        resource_type: The type of resource ('groups' or 'projects')
        resource_id: The ID or URL-encoded path of the project or group
        email: The email address the invitation was previously sent to
        access_level: A valid access level (defaults: 30, the Developer role)
        expires_at: A date string in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        
    Returns:
        Returns information about an updated invitation including access level, creation details, creator information, and expiration date."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Ensure resource_type is either 'groups' or 'projects'
    if resource_type not in ['groups', 'projects']:
        raise ValueError("resource_type must be either 'groups' or 'projects'")
    
    # URL encode the email address
    encoded_email = quote(email)
    
    # Build the URL
    url = f"{base_url}/{resource_type}/{resource_id}/invitations/{encoded_email}"
    
    # Prepare parameters
    params = {'access_level': access_level}
    if expires_at:
        params['expires_at'] = expires_at
    
    # Make the API call
    response = requests.put(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = update_invitation(resource_type='projects', resource_id=183, email='test@example.com', access_level=40)
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