import requests, json
from urllib.parse import quote



def search_groups(search_term: str, search_in: str = 'name_path', visibility: str = None, order_by: str = None, sort: str = 'asc', per_page: int = 20, page: int = 1) -> list:
    """
    Searches for GitLab groups matching the specified term in their name or path. Returns a list of matching groups with their details including ID, name, path, and description.
    
    Args:
        search_term (str): The search term to find in group names and paths
        search_in (str, optional): Where to search for the term. Defaults to 'name_path'.
        visibility (str, optional): Filter by visibility. Defaults to None.
        order_by (str, optional): Order results by this field. Defaults to None.
        sort (str, optional): Sort order, either 'asc' or 'desc'. Defaults to 'asc'.
        per_page (int, optional): Number of results per page. Defaults to 20.
        page (int, optional): Page number. Defaults to 1.
        
    Returns:
        Returns a list of GitLab groups matching the search term with their ID, name, path, and description."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/groups"
    
    params = {
        'search': search_term,
    }
    
    if search_in:
        params['search_in'] = search_in
    if visibility:
        params['visibility'] = visibility
    if order_by:
        params['order_by'] = order_by
    if sort:
        params['sort'] = sort
    if per_page:
        params['per_page'] = per_page
    if page:
        params['page'] = page
    
    return requests.get(url, headers=headers, params=params)

if __name__ == '__main__':
    r = search_groups(search_term="foobar")
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