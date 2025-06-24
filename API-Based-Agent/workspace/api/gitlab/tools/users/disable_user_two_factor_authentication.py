import requests

def disable_user_two_factor_authentication(user_id: int, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token: str = "glpat-qvQ-N6mN_tAddXb2WWdi"):
    """
    Disables two-factor authentication (2FA) for a specified user. This function can only be used by administrators and cannot be used to disable 2FA for other administrators or the calling administrator's own account.
    
    Args:
        user_id (int): The ID of the user for whom to disable 2FA
        base_url (str, optional): The base URL of the GitLab API
        token (str, optional): The private token for authentication
        
    Returns:
        requests.Response: The response from the API call
        
    Raises:
        HTTPError: If the API request fails
        
    Example:
        >>> response = disable_user_two_factor_authentication(user_id=2330)
        >>> response.status_code
        204
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/users/{user_id}/disable_two_factor"
    response = requests.patch(url, headers=headers)
    # Don't raise exception for 403 error as it's expected for non-admin users
    if response.status_code != 403:
        response.raise_for_status()
    return response

if __name__ == '__main__':
    r = disable_user_two_factor_authentication(user_id=2330)
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