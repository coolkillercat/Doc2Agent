import requests, json
from urllib.parse import quote

def reject_user(user_id: int, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token: str = "glpat-qvQ-N6mN_tAddXb2WWdi") -> dict:
    """
    Rejects a user who is pending approval in GitLab. This function is available only for administrators and returns the result of the rejection operation.
    
    Args:
        user_id (int): The ID of the user to reject
        base_url (str, optional): The base URL of the GitLab API
        token (str, optional): The private token for authentication
        
    Returns:
        dict: The response from the API request
        
    Example:
        >>> reject_user(2330)
        {'message': 'Success'}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/users/{user_id}/reject"
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text, "status_code": response.status_code}

if __name__ == '__main__':
    r = reject_user(user_id=2330)
    r_json = None
    try:
        if isinstance(r, dict) and 'error' in r:
            r_json = r
            status_code = r.get('status_code')
            text = r.get('error')
            content = r.get('error')
        else:
            r_json = r
            status_code = 200
            text = json.dumps(r)
            content = json.dumps(r)
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = status_code
    result_dict['text'] = text
    result_dict['json'] = r_json
    result_dict['content'] = content
    print(json.dumps(result_dict, indent=4))