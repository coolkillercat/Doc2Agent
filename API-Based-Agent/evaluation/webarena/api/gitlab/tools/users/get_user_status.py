import requests, json
from urllib.parse import quote



def get_user_status(id_or_username: str):
    """
    Retrieves the current status of a GitLab user including their emoji, availability, message, and clear status time. Useful for checking a user's availability before collaboration or communication.
    
    Args:
        id_or_username (str): ID or username of the user to get a status of
        
    Returns:
        Returns a GitLab user's status information including their emoji, availability, message, and scheduled clear time."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4'
    url = f"{base_url}/users/{quote(str(id_or_username))}/status"
    
    return requests.get(url, headers=headers)

if __name__ == '__main__':
    r = get_user_status(id_or_username="byteblaze")
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