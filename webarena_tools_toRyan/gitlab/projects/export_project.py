import requests, json
from urllib.parse import quote



def export_project(project_id: str, export_format: str = 'json', include_archived: bool = False, include_relations: bool = True) -> bytes:
    """
    Exports a project with all its data in the specified format, allowing for project backup, migration, or sharing. Options control whether to include archived items and related entities.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project.
        export_format (str, optional): Format of the export. Options: 'json', 'xml', etc. Defaults to 'json'.
        include_archived (bool, optional): Include archived projects in the export. Defaults to False.
        include_relations (bool, optional): Include relations in the export. Defaults to True.
    
    Returns:
        Returns the exported project data in the requested format, including project details and optionally archived items and relations."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/export"
    
    params = {
        'download': True,
        'include_archived': include_archived,
        'include_relations': include_relations
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ == '__main__':
    r = export_project(project_id='183', export_format='json')
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