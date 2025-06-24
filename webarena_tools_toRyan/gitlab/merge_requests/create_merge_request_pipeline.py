import requests
from urllib.parse import quote


def create_merge_request_pipeline(project_id, merge_request_iid, base_url="http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4", token="GITLAB_KEY_REMOVED"):
    """
    Creates a pipeline for a merge request, which can be a detached merge request pipeline or a merged results pipeline depending on project settings.
    This enables CI/CD workflows specifically for merge request validation.
    
    Args:
        project_id (int or str): The ID or URL-encoded path of the project owned by the authenticated user.
        merge_request_iid (int): The internal ID of the merge request.
        base_url (str, optional): The base URL for the GitLab API.
        token (str, optional): The private token for authentication.
    
    Returns:
        Response object from the API call.
    
    Example:
        >>> create_merge_request_pipeline(project_id=183, merge_request_iid=1)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': token}
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/merge_requests/{merge_request_iid}/pipelines"
    response = requests.post(url, headers=headers)
    return response


if __name__ == '__main__':
    r = create_merge_request_pipeline(project_id=183, merge_request_iid=1)
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