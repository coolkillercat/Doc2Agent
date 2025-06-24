import requests, json
from urllib.parse import quote



def list_user_projects(username: str) -> list:
    """
    Retrieves a list of projects associated with a specific user. This helps in discovering and accessing user-created content or contributions.
    
    Args:
        username (str): The username of the user whose projects you want to list
        
    Returns:
        Returns a list of projects associated with a specific user, including project details, repository information, and access permissions."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_username = quote(username, safe='')
    url = f"{base_url}/users/{encoded_username}/projects"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = list_user_projects(username="byteblaze")
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