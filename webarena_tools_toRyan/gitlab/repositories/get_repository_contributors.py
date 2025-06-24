import requests, json
from urllib.parse import quote



def get_repository_contributors(project_id, order_by='commits', sort='asc'):
    """
    Retrieves a list of contributors for a specific repository, showing their names, emails, commit counts, additions, and deletions. Can be sorted by different attributes to identify key contributors.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project.
        order_by (str, optional): Order contributors by 'name', 'email', or 'commits'. Default is 'commits'.
        sort (str, optional): Sort order, either 'asc' or 'desc'. Default is 'asc'.
        
    Returns:
        Returns a list of repository contributors with their names, emails, commit counts, additions, and deletions."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    # Construct URL with proper encoding for project_id
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/repository/contributors"
    
    # Add query parameters
    params = {
        'order_by': order_by,
        'sort': sort
    }
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    return response

if __name__ == '__main__':
    r = get_repository_contributors(project_id=183, order_by='commits', sort='desc')
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