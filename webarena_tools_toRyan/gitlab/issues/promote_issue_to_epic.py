import requests, json
from urllib.parse import quote



def promote_issue_to_epic(project_id: str, issue_iid: int, comment: str = ''):
    """
    Promotes an existing issue to an epic by adding a comment with the /promote quick action. Optionally includes additional comment text along with the promotion command.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        issue_iid (int): The internal ID of the project's issue
        comment (str, optional): Additional comment text to include with the promotion. Defaults to empty string.
    
    Returns:
        Returns a note object containing the comment with the promotion command and associated metadata about the issue promotion."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    # Format the body to include the /promote command
    if comment:
        body = f"{comment}\n\n/promote"
    else:
        body = "/promote"
    
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{project_id}/issues/{issue_iid}/notes"
    
    data = {"body": body}
    
    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == '__main__':
    r = promote_issue_to_epic(project_id=183, issue_iid=1, comment="Let's promote this issue to an epic")
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