import requests, json
from urllib.parse import quote


def update_project_milestone(project_id: str, milestone_id: int, title: str = None, description: str = None, due_date: str = None, start_date: str = None, state_event: str = None) -> dict:
    """
    Updates an existing project milestone with specified details such as title, description, dates, and state.
    Allows project managers to modify milestone information to reflect changes in project planning and tracking.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        milestone_id (int): The ID of the project's milestone to update
        title (str, optional): The new title of the milestone
        description (str, optional): The new description of the milestone
        due_date (str, optional): The new due date of the milestone (YYYY-MM-DD)
        start_date (str, optional): The new start date of the milestone (YYYY-MM-DD)
        state_event (str, optional): The state event of the milestone (close or activate)
        
    Returns:
        dict: The response from the API containing the updated milestone information
        
    Example:
        >>> update_project_milestone(
        ...     project_id="183", 
        ...     milestone_id=1, 
        ...     title="Updated Milestone", 
        ...     description="This milestone has been updated", 
        ...     due_date="2023-12-31"
        ... )
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/milestones/{milestone_id}"
    
    payload = {}
    if title is not None:
        payload["title"] = title
    if description is not None:
        payload["description"] = description
    if due_date is not None:
        payload["due_date"] = due_date
    if start_date is not None:
        payload["start_date"] = start_date
    if state_event is not None:
        payload["state_event"] = state_event
    
    response = requests.put(url, headers=headers, json=payload)
    return response.json() if response.status_code == 200 else response


if __name__ == '__main__':
    r = update_project_milestone(project_id=183, milestone_id=1, title="Updated Milestone", description="This milestone has been updated", due_date="2023-12-31")
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