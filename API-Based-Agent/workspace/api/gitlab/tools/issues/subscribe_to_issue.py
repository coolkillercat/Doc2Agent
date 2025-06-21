import requests, json
from urllib.parse import quote



def subscribe_to_issue(project_id: str, issue_iid: int) -> dict:
    """
    Subscribes the authenticated user to a specific issue to receive notifications about updates and changes to that issue.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the project's issue
        
    Returns:
        Returns issue details with subscription status after subscribing the authenticated user to receive notifications for a specific issue."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id))}/issues/{issue_iid}/subscribe"
    
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = subscribe_to_issue(project_id=183, issue_iid=1)
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