import requests
from urllib.parse import quote


def start_pull_mirroring(project_id):
    """
    Initiates the pull mirroring process for a GitLab project, allowing the project to be updated with changes from its configured mirror source.

    Args:
        project_id (str or int): The ID or URL-encoded path of the project.

    Returns:
        requests.Response: The response from the API.

    Example:
        >>> response = start_pull_mirroring(183)
        >>> response.status_code
        200
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    # Ensure project_id is properly encoded
    encoded_project_id = quote(str(project_id), safe='')
    url = f"{base_url}/projects/{encoded_project_id}/mirror/pull"
    
    response = requests.post(url, headers=headers)
    return response


if __name__ == '__main__':
    r = start_pull_mirroring(project_id=183)
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