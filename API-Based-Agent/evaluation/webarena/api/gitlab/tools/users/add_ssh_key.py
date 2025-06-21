import requests, json
from urllib.parse import quote



def add_ssh_key(title: str, key: str, expires_at: str = None, usage_type: str = 'auth_and_signing'):
    """
    Creates a new SSH key for the authenticated user with specified title, key content, optional expiration date, and usage scope (authentication, signing, or both).
    
    Args:
        title (str): Title for the SSH key
        key (str): The SSH key content
        expires_at (str, optional): Expiration date in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        usage_type (str, optional): Scope of usage - 'auth', 'signing', or 'auth_and_signing'. Default: 'auth_and_signing'
    
    Returns:
        Returns information about the newly created SSH key including its ID, title, creation date, expiration status, key content, and usage type."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/user/keys"
    
    payload = {
        "title": title,
        "key": key,
        "usage_type": usage_type
    }
    
    if expires_at:
        payload["expires_at"] = expires_at
        
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = add_ssh_key(
        title="Test SSH Key",
        key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFrUTme9tZ2G+tfRpOheHEAGXWCYAUAx4bCvJqJNSd7Dxt0AsDiEpgOHNNAWXXCbmsjsPzRuU6XWYJlNbKPQ9LE2mJdV8AV6subUZY4eurLAQc06lZWZEXYx7SQppUxwPpjZK2CbUAZvLLO7/bVQCl8GSNLOws3zrThXsAnFnRLO/EsVUX+l6tpL4/J93rZP2C7D60zHUbGZxHn9eZ9EXNFP7TyjqBb/Gm9Q1EXJlzIQtydOBG1bXcnDQSNfJXQMyzmrF1YSY7u0SGXL9cgszrjfXRWgmzPtzDZOh7bO34Bb9qkxkQG/mVcvW8QJhtgJ3k4xllEb2yZ7+jHJ/MUaaN test@example.com"
    )
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