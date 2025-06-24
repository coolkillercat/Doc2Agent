import requests, json
from urllib.parse import quote



def list_ssh_keys(page: int = 1, per_page: int = 30) -> requests.Response:
    """
    Retrieves a list of the authenticated user's SSH keys with optional pagination. Returns details including key ID, title, public key content, and creation date.
    
    Args:
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of items per page. Defaults to 30.
        
    Returns:
        Returns a list of the authenticated user's SSH keys including ID, title, public key content, and creation date."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/user/keys?page={page}&per_page={per_page}"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = list_ssh_keys(page=1, per_page=10)
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