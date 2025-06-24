import requests, json
from urllib.parse import quote



def generate_changelog(project_id: int, version: str, config_file: str = None, date: str = None, from_commit: str = None, to_commit: str = None, trailer: str = None) -> dict:
    """
    Generates changelog data for a project based on commits without committing to a changelog file. Returns formatted notes that summarize changes between commits following semantic versioning conventions.
    
    Args:
        project_id (int): The ID of the project
        version (str): The version to generate the changelog for (must follow semantic versioning)
        config_file (str, optional): Path to changelog configuration file in the repository
        date (str, optional): Date and time of the release in ISO 8601 format (e.g., '2016-03-11T03:45:40Z')
        from_commit (str, optional): Start of the commit range (SHA) for changelog generation
        to_commit (str, optional): End of the commit range (SHA) for changelog generation
        trailer (str, optional): Git trailer to use for including commits
        
    Returns:
        Returns formatted changelog notes that summarize changes between commits following semantic versioning conventions."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/repository/changelog"
    
    params = {'version': version}
    
    if config_file:
        params['config_file'] = config_file
    if date:
        params['date'] = date
    if from_commit:
        params['from'] = from_commit
    if to_commit:
        params['to'] = to_commit
    if trailer:
        params['trailer'] = trailer
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = generate_changelog(project_id=183, version="1.0.0")
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