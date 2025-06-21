import requests, json
from urllib.parse import quote



def get_member_details(source_type: str, source_id: str, user_id: int):
    """
    Retrieves detailed information about a specific member of a group or project, including inherited and invited members.
    
    Args:
        source_type (str): The type of the source ('group' or 'project')
        source_id (str): The ID or URL-encoded path of the group or project
        user_id (int): The user ID of the member
    
    Returns:
        Returns detailed information about a specific member of a group or project, including their access level, creation details, and membership status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_id = quote(str(source_id), safe='')
    
    if source_type.lower() == 'group':
        url = f"{base_url}/groups/{encoded_id}/members/all/{user_id}"
    elif source_type.lower() == 'project':
        url = f"{base_url}/projects/{encoded_id}/members/all/{user_id}"
    else:
        raise ValueError("source_type must be either 'group' or 'project'")
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_member_details(source_type='project', source_id='183', user_id=2330)
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