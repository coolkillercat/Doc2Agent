import requests, json
from urllib.parse import quote

def get_user_ssh_key(user_id: int, key_id: int):
    """
    Retrieves a specific SSH key for a given GitLab user. This allows administrators or authorized users to verify SSH key details for authentication and access management purposes.
    
    Args:
        user_id (int): The ID of the user whose SSH key is to be retrieved
        key_id (int): The ID of the SSH key to retrieve
        
    Returns:
        Response: The HTTP response object containing the SSH key information
        
    Example:
        >>> response = get_user_ssh_key(user_id=2330, key_id=1)
        >>> print(response.status_code)
        200
        >>> print(response.json())
        {'id': 1, 'title': 'Public key', 'key': 'ssh-rsa AAAA...', 'created_at': '2014-08-01T14:47:39.080Z'}
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/users/{user_id}/keys/{key_id}"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_user_ssh_key(user_id=2330, key_id=1)
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