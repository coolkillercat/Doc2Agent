import requests, json
from urllib.parse import quote



def get_project_templates(project_id: str, template_type: str):
    """
    Retrieves all templates of a specified type for a given project. Allows users to access various templates such as dockerfiles, gitignores, licenses, and more to incorporate into their project.
    
    Args:
        project_id (str): The ID or URL-encoded path of the project
        template_type (str): The type of the template. Accepted values are: 'dockerfiles', 'gitignores', 'gitlab_ci_ymls', 'licenses', 'issues', or 'merge_requests'
        
    Returns:
        Returns a list of project templates of a specified type (such as dockerfiles, licenses, or gitignores) with their keys and names."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi', }
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/templates/{template_type}"
    
    return requests.get(url, headers=headers)

if __name__ == '__main__':
    r = get_project_templates(project_id="183", template_type="licenses")
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