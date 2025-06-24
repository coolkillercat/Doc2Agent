import requests
from urllib.parse import quote

def download_project_avatar(project_id: str, base_url: str = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token: str = "glpat-qvQ-N6mN_tAddXb2WWdi") -> bytes:
    """
    Downloads a project's avatar image. Returns the avatar image data as bytes which can be saved or displayed.
    
    Args:
        project_id (str): ID or URL-encoded path of the project
        base_url (str, optional): Base URL for the GitLab API
        token (str, optional): Private token for authentication
        
    Returns:
        bytes: The avatar image data
        
    Example:
        >>> avatar_data = download_project_avatar('183')
        >>> with open('project_avatar.png', 'wb') as f:
        ...     f.write(avatar_data)
    """
    headers = {'PRIVATE-TOKEN': token}
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/avatar"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = download_project_avatar(project_id='183')
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