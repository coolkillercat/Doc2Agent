import requests, json
from urllib.parse import quote



def get_user_contribution_events(username: str, from_date: str = None, to_date: str = None, per_page: int = 30, page: int = 1):
    """
    Retrieves contribution events for a specified GitLab user within an optional date range.
    
    Args:
        username: The username of the GitLab user
        from_date: Optional start date in ISO format (e.g., 2023-01-01)
        to_date: Optional end date in ISO format (e.g., 2023-12-31)
        per_page: Number of events per page (default: 30)
        page: Page number (default: 1)
    
    Returns:
        Returns a list of contribution events for a specified GitLab user, including action details, timestamps, and author information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/users/{quote(username)}/events"
    
    params = {
        'per_page': per_page,
        'page': page
    }
    
    if from_date:
        params['after'] = from_date
    
    if to_date:
        params['before'] = to_date
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_user_contribution_events(username="byteblaze", from_date="2023-01-01", to_date="2023-12-31", per_page=10, page=1)
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