import requests, json
from urllib.parse import quote



def create_milestone(project_id: int or str, title: str, description: str = None, due_date: str = None, start_date: str = None):
    """
    Creates a new milestone for a project with the specified title and optional details such as description, due date, and start date.
    
    Args:
        project_id (int or str): The ID of the project
        title (str): The title of the milestone
        description (str, optional): The description of the milestone
        due_date (str, optional): The due date of the milestone (YYYY-MM-DD)
        start_date (str, optional): The start date of the milestone (YYYY-MM-DD)
        
    Returns:
        Returns detailed information about the newly created project milestone, including its ID, title, description, dates, and status."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(str(project_id), safe='')}/milestones"
    
    payload = {
        "title": title
    }
    
    if description:
        payload["description"] = description
    if due_date:
        payload["due_date"] = due_date
    if start_date:
        payload["start_date"] = start_date
    
    return requests.post(url, headers=headers, json=payload)

if __name__ == '__main__':
    r = create_milestone(project_id=183, title="New Release Milestone", description="This is a test milestone", due_date="2023-12-31", start_date="2023-10-01")
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