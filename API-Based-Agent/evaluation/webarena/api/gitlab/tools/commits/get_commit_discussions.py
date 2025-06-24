import requests
from urllib.parse import quote


def get_commit_discussions(project_id, commit_id):
    """
    Retrieves all discussion threads for a specific commit in a project, including comments, replies, and diff notes.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project
        commit_id (str): The SHA of the commit
        
    Returns:
        requests.Response: The API response containing commit discussions
        
    Example:
        >>> get_commit_discussions(183, "68d109f3e03c9c5d130fc0f35f5a874a20efa956")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(str(project_id), safe='')}/repository/commits/{quote(str(commit_id), safe='')}/discussions"
    
    response = requests.get(url, headers=headers)
    return response


if __name__ == '__main__':
    r = get_commit_discussions(project_id=183, commit_id="68d109f3e03c9c5d130fc0f35f5a874a20efa956") 
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