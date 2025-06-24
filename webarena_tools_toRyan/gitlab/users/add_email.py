import requests, json
from urllib.parse import quote



def add_email(email: str) -> dict:
    """
    Creates a new email address for the authenticated user's account, enabling them to receive notifications and communications to this additional email.
    
    Args:
        email (str): The email address to add to the user's account
        
    Returns:
        Returns information about the newly created email address including its ID and confirmation status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"{base_url}/user/emails"
    payload = {"email": email}
    
    response = requests.post(endpoint, headers=headers, json=payload)
    
    return response

if __name__ == '__main__':
    r = add_email(email="test_email@example.com")
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