import requests, json
from urllib.parse import quote



def get_user_gpg_keys(user_id: int):
    """
    Retrieves all GPG keys associated with a specific GitLab user. Useful for verifying a user's identity or for secure communication purposes.
    
    Args:
        user_id (int): The ID of the user whose GPG keys are to be retrieved
        
    Returns:
        Returns a list of GPG keys associated with a specific GitLab user."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    endpoint = f"/users/{user_id}/gpg_keys"
    url = base_url + endpoint
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_user_gpg_keys(user_id=2330)
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