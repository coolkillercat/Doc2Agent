import requests, json
from urllib.parse import quote

def get_project_push_rules(project_id: str) -> dict:
    """
    Retrieves the push rules configuration for a specific GitLab project, allowing users to view rules that enforce commit format, branch naming, security checks, and other repository constraints.
    
    Args:
        project_id (str): The ID or URL-encoded path of the GitLab project
        
    Returns:
        dict: The JSON response containing the push rules configuration
        
    Example:
        >>> get_project_push_rules('183')
        {
            "id": 1,
            "project_id": 183,
            "commit_message_regex": "Fixes \\d+\\..*",
            "commit_message_negative_regex": "ssh\\:\\/\\/",
            ...
        }
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{quote(str(project_id), safe='')}/push_rule"
    
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response

if __name__ == '__main__':
    r = get_project_push_rules(project_id='183')
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