import requests, json
from urllib.parse import quote


def get_project_template(project_id: str, template_type: str, template_name: str, fullname: str = None, project_name: str = None, source_template_project_id: int = None) -> dict:
    """
    Retrieves a specific template (Dockerfile, GitIgnore, CI/CD configuration, license, issue, or merge request) from a project to use as a starting point for new files or configurations.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        template_type (str): The type of the template. One of: 'dockerfiles', 'gitignores', 'gitlab_ci_ymls', 'licenses', 'issues', or 'merge_requests'.
        template_name (str): The key of the template, as obtained from the collection endpoint.
        fullname (str, optional): The full name of the copyright holder to use when expanding placeholders in the template. Affects only licenses.
        project_name (str, optional): The project name to use when expanding placeholders in the template. Affects only licenses.
        source_template_project_id (int, optional): The project ID where a given template is being stored.
    
    Returns:
        Returns a specific project template (Dockerfile, GitIgnore, CI/CD configuration, license, issue, or merge request) with its content and metadata."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    encoded_template_name = quote(template_name, safe='')
    url = f"{base_url}/projects/{project_id}/templates/{template_type}/{encoded_template_name}"
    
    params = {}
    if fullname:
        params['fullname'] = fullname
    if project_name:
        params['project'] = project_name
    if source_template_project_id:
        params['source_template_project_id'] = source_template_project_id
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = get_project_template(project_id=183, template_type="licenses", template_name="mit", fullname="ByteBlaze Inc")
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