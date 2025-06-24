import requests, json
from urllib.parse import quote

def auth_register(email, password, **kwargs):
    """
    Register a new user account with the GlyGen API.
    
    Args:
        email (str): Email address for the new user account
        password (str): Password for the new user account
        **kwargs: Additional parameters to include in the registration payload
    
    Returns:
        requests.Response: The API response containing registration status
        
    Example:
        >>> response = auth_register('newuser@example.com', 'securepassword')
    """
    api_url = "https://api.glygen.org/auth/register/"
    
    payload = {
        'email': email,
        'password': password,
        **kwargs
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = auth_register(email='newuser@example.com', password='securepassword')
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