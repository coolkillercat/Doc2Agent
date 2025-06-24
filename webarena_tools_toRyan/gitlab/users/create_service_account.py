import requests, json
from urllib.parse import quote


def create_service_account(name: str = None, username: str = None) -> dict:
    """
    Creates a service account user for automated processes or integrations. Returns the service account details including ID, username, and name.
    
    Args:
        name (str, optional): Name of the service account user. Defaults to None.
        username (str, optional): Username of the service account user. Defaults to None.
        
    Returns:
        dict: Response from the API containing the created service account details
        
    Examples:
        >>> create_service_account(name="Test Service Account", username="test_service_account")
        >>> create_service_account(name="Automation Bot")
        >>> create_service_account(username="automation_service")
        >>> create_service_account()
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    url = f"{base_url}/service_accounts"
    
    payload = {}
    if name:
        payload['name'] = name
    if username:
        payload['username'] = username
    
    response = requests.post(url, headers=headers, json=payload)
    
    return response.json() if response.status_code == 201 else response

if __name__ == '__main__':
    r = create_service_account(name="Test Service Account", username="test_service_account")
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