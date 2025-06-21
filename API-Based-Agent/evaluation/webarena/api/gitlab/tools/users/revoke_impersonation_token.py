import requests, json
from urllib.parse import quote

def revoke_impersonation_token(user_id: int, impersonation_token_id: int, base_url: str = None, token: str = None):
    """
    Revokes a specific impersonation token for a user. This is an administrative function that permanently invalidates the specified token, preventing further API access using that token.
    
    Args:
        user_id (int): ID of the user whose token will be revoked
        impersonation_token_id (int): ID of the impersonation token to revoke
        base_url (str, optional): Base URL for the GitLab API. Defaults to configured URL.
        token (str, optional): Private token for authentication. Defaults to configured token.
        
    Returns:
        Response object from the API call
        
    Example:
        >>> revoke_impersonation_token(user_id=2330, impersonation_token_id=123)
    """
    if base_url is None:
        base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    if token is None:
        token = "glpat-qvQ-N6mN_tAddXb2WWdi"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    
    url = f"{base_url}/users/{user_id}/impersonation_tokens/{impersonation_token_id}"
    
    response = requests.delete(url, headers=headers)
    return response

if __name__ == '__main__':
    r = revoke_impersonation_token(user_id=2330, impersonation_token_id=123)
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