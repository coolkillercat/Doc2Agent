import requests, json
from urllib.parse import quote



def search_projects(search: str, order_by: str = None, sort: str = None) -> list:
    """
    Search for GitLab projects by name that are accessible to the authenticated user. Returns a list of matching projects sorted according to the specified criteria.
    
    Args:
        search (str): A string contained in the project name.
        order_by (str, optional): Return requests ordered by 'id', 'name', 'created_at' or 'last_activity_at' fields.
        sort (str, optional): Return requests sorted in 'asc' or 'desc' order.
        
    Returns:
        Returns a list of GitLab projects matching the search criteria with detailed project information including metadata, settings, and permissions."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects"
    
    params = {'search': search}
    
    if order_by:
        params['order_by'] = order_by
    
    if sort:
        params['sort'] = sort
    
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = search_projects(search="test", order_by="name", sort="asc")
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