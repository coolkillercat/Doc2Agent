import requests, json
from urllib.parse import quote

def get_user_gpg_key(key_id: int) -> dict:
    """
    Retrieves a specific GPG key for the authenticated user by its ID. Returns detailed information about the requested GPG key including the full public key and creation date.
    
    Args:
        key_id (int): ID of the GPG key to retrieve
        
    Returns:
        Returns detailed information about a specific GPG key for the authenticated user, including the key ID, full public key content, and creation date.
    Example:
        >>> get_user_gpg_key(1)
        {
            "id": 1,
            "key": "-----BEGIN PGP PUBLIC KEY BLOCK-----...",
            "created_at": "2017-09-05T09:17:46.264Z"
        }
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/user/gpg_keys/{key_id}"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_user_gpg_key(key_id=1)
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