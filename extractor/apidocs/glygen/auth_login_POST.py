import requests
import json

def auth_login(email, password):
    """
    Authenticate a user with the GlyGen API.
    
    Args:
        email (str): User's email address
        password (str): User's password
    
    Returns:
        requests.Response: The API response object
    
    Example:
        >>> response = auth_login('user@example.com', 'password123')
        >>> if response.status_code == 200:
        >>>     print("Login successful")
        >>> else:
        >>>     print("Login failed")
    """
    api_url = "https://api.glygen.org/auth/login/"
    
    # Create payload with required parameters
    payload = {
        "email": email,
        "password": password
    }
    
    # Send request to API
    response = requests.post(
        url=api_url,
        json=payload,
        timeout=50
    )
    
    return response

if __name__ == '__main__':
    r = auth_login(email='user@example.com', password='password123')
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