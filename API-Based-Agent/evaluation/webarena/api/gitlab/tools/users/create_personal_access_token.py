import requests, json
from urllib.parse import quote

def create_personal_access_token(name: str, expires_at: str = None) -> dict:
    """
    Creates a new personal access token for the currently authenticated user with k8s_proxy scope.
    Returns the token details including the one-time accessible token value.
    
    Args:
        name (str): Name of the personal access token
        expires_at (str, optional): Expiration date of the access token in ISO format (YYYY-MM-DD).
                    If not provided, the token expires at the end of the current day.
    
    Returns:
        dict: The API response as a dictionary
    
    Example:
        >>> create_personal_access_token(name="test_token", expires_at="2023-12-31")
        {
            "id": 3,
            "name": "test_token",
            "revoked": false,
            "created_at": "2023-10-14T11:58:53.526Z",
            "scopes": ["k8s_proxy"],
            "user_id": 42,
            "active": true,
            "expires_at": "2023-12-31",
            "token": "<your_new_access_token>"
        }
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/user/personal_access_tokens"
    
    payload = {
        "name": name,
        "scopes": ["k8s_proxy"]
    }
    
    if expires_at:
        payload["expires_at"] = expires_at
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    return response

if __name__ == '__main__':
    r = create_personal_access_token(name="test_token", expires_at="2023-12-31")
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