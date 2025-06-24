import requests, json
from urllib.parse import quote

def get_resource_events(resource_id: str, resource_type: str = "issues", event_type: str = None, page: int = 1, per_page: int = 20):
    """
    Retrieves events associated with a specific resource, with optional filtering by event type. Allows monitoring of resource-related activities such as label changes, state updates, milestone assignments, weight modifications, and iteration changes.
    
    Args:
        resource_id (str): The ID of the resource to get events for
        resource_type (str, optional): The type of resource (issues, merge_requests, etc.). Defaults to "issues".
        event_type (str, optional): The type of event to filter by. Defaults to None.
        page (int, optional): The page number of results to retrieve. Defaults to 1.
        per_page (int, optional): The number of results per page. Defaults to 20.
        
    Returns:
        requests.Response: The response from the API call
        
    Examples:
        >>> get_resource_events(resource_id="1", resource_type="issues")
        >>> get_resource_events(resource_id="83730", resource_type="issues", event_type="state")
        >>> get_resource_events(resource_id="56150", resource_type="merge_requests", page=2, per_page=10)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/183/{resource_type}/{resource_id}/resource_events"
    
    params = {
        'page': page,
        'per_page': per_page
    }
    
    if event_type:
        params['action_type'] = event_type
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_resource_events(resource_id="1", resource_type="issues")
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