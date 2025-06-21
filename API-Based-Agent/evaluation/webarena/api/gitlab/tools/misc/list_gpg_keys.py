import requests, json
from urllib.parse import quote



def list_gpg_keys() -> list:
    """
    Retrieves all GPG keys associated with the authenticated user's GitLab account. This helps users manage their encryption keys for secure Git operations.
    
    Returns:
        Returns a list of GPG keys associated with the authenticated user's GitLab account."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/user/gpg_keys"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = list_gpg_keys()
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