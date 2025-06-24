import requests
from urllib.parse import quote

def get_group_namespaces(group_id: str, per_page: int = 20, page: int = 1) -> dict:
    """
    Retrieves namespaces within a specified group with pagination support. Allows users to control the number of results per page and navigate through multiple pages of namespaces.
    
    Args:
        group_id (str): The ID of the group to retrieve namespaces from
        per_page (int, optional): Number of namespaces to return per page (max 100). Defaults to 20.
        page (int, optional): Page number of results to fetch. Defaults to 1.
    
    Returns:
        dict: Response object from the API call
        
    Example:
        >>> get_group_namespaces(group_id="183", per_page=30, page=1)
        <Response [200]>
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups/{quote(str(group_id))}/namespaces?per_page={per_page}&page={page}"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_group_namespaces(group_id="183", per_page=30, page=1)
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