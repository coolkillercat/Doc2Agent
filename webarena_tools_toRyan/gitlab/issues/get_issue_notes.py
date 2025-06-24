import requests, json
from urllib.parse import quote



def get_issue_notes(project_id: str, issue_iid: int, sort: str = 'desc', order_by: str = 'created_at'):
    """
    Retrieves all notes for a specific issue in a project, with options to sort and order the results.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The IID of the issue
        sort (str, optional): Return issue notes sorted in 'asc' or 'desc' order. Defaults to 'desc'.
        order_by (str, optional): Return issue notes ordered by 'created_at' or 'updated_at'. Defaults to 'created_at'.
    
    Returns:
        Returns a list of notes for a specific issue in a project, including author details, content, timestamps, and system information."""
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/issues/{issue_iid}/notes"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    params = {
        'sort': sort,
        'order_by': order_by
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_issue_notes(project_id=183, issue_iid=1, sort='desc', order_by='created_at')
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