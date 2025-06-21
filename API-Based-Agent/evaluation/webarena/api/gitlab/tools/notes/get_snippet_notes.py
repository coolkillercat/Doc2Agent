import requests
from urllib.parse import quote

def get_snippet_notes(project_id, snippet_id, sort='desc', order_by='created_at'):
    """
    Retrieves all notes (comments) for a specific project snippet, with optional sorting parameters to control the order of results.
    
    Args:
        project_id (str or int): The ID or URL-encoded path of the project
        snippet_id (int): The ID of the project snippet
        sort (str, optional): Return snippet notes sorted in 'asc' or 'desc' order. Default is 'desc'
        order_by (str, optional): Return snippet notes ordered by 'created_at' or 'updated_at' fields. Default is 'created_at'
        
    Returns:
        Response object containing the snippet notes
        
    Example:
        >>> get_snippet_notes(project_id=183, snippet_id=1)
        >>> get_snippet_notes(project_id=183, snippet_id=1, sort='asc', order_by='updated_at')
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Handle URL encoding for project_id if it's a string path
    if isinstance(project_id, str) and '/' in project_id:
        project_id = quote(project_id, safe='')
    
    url = f"{base_url}/projects/{project_id}/snippets/{snippet_id}/notes"
    
    params = {
        'sort': sort,
        'order_by': order_by
    }
    
    return requests.get(url, headers=headers, params=params)

if __name__ == '__main__':
    r = get_snippet_notes(project_id=183, snippet_id=1)
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