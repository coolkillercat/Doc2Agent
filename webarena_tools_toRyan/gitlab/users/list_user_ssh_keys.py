import requests, json
from urllib.parse import quote



def list_user_ssh_keys(id_or_username: str):
    """
    Retrieves all SSH keys associated with a specific user, identified by either their user ID or username.
    
    Args:
        id_or_username (str): The ID or username of the user to get the SSH keys for.
        
    Returns:
        Returns a list of SSH keys associated with a specified user identified by their ID or username."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/users/{quote(str(id_or_username))}/keys"
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = list_user_ssh_keys(id_or_username="byteblaze")
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