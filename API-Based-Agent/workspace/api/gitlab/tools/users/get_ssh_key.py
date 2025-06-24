import requests, json
from urllib.parse import quote

def get_ssh_key(key_id: str) -> dict:
    """
    Retrieve details of a specific SSH key associated with the user account.
    
    Args:
        key_id (str): ID of the SSH key to retrieve
        
    Returns:
        dict: Response object containing the SSH key details including ID, title, 
              public key content, and creation timestamp
    
    Example:
        >>> get_ssh_key("1")
        {
            "id": 1,
            "title": "Public key",
            "key": "ssh-rsa AAAAB3NzaC1yc2EAAAA...",
            "created_at": "2014-08-01T14:47:39.080Z"
        }
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/user/keys/{quote(str(key_id))}"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_ssh_key(key_id="1")  # Using key_id=1 as a test parameter
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