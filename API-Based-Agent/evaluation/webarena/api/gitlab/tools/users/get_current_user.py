import requests, json
from urllib.parse import quote



def get_current_user(sudo_id: int = None) -> dict:
    """
    Retrieves information about the currently authenticated user. Administrators can optionally retrieve information for a specific user by providing their ID in the sudo parameter.
    
    Args:
        sudo_id (int, optional): ID of a user to make the call in their place. Defaults to None.
        
    Returns:
        Returns detailed profile information about the currently authenticated user, including personal details, account settings, and activity statistics."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4'
    url = f"{base_url}/user"
    
    params = {}
    if sudo_id is not None:
        params['sudo'] = sudo_id
    
    return requests.get(url, headers=headers, params=params)

if __name__ == '__main__':
    r = get_current_user()
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