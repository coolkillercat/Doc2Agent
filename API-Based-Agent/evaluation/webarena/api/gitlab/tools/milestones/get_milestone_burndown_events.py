import requests
from urllib.parse import quote

def get_milestone_burndown_events(project_id, milestone_id):
    """
    Retrieves all burndown chart events for a specific milestone in a project, providing data to track progress against timeline targets.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project owned by the authenticated user
        milestone_id (int): The ID of the project's milestone
        
    Returns:
        requests.Response: The API response containing burndown chart events for the specified milestone
        
    Example:
        >>> response = get_milestone_burndown_events(project_id=183, milestone_id=1)
        >>> print(response.status_code)
        200
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_project_id = quote(str(project_id), safe='')
    url = f"{base_url}/projects/{encoded_project_id}/milestones/{milestone_id}/burndown_events"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_milestone_burndown_events(project_id=183, milestone_id=1)
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