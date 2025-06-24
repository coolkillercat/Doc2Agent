import requests, json
from urllib.parse import quote



def unarchive_project(project_id: str):
    """
    Unarchives a GitLab project, making it active again. This tool is useful for project administrators or owners who need to restore an archived project to active status.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project to unarchive
        
    Returns:
        Returns comprehensive details of the unarchived project including its metadata, settings, permissions, and repository information."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(str(project_id), safe='')}/unarchive"
    response = requests.post(url, headers=headers)
    return response

if __name__ == '__main__':
    r = unarchive_project(project_id='183')
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