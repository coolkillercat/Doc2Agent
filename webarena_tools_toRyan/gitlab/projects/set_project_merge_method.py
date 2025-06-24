import requests, json
from urllib.parse import quote



def set_project_merge_method(project_id: int, merge_method: str) -> dict:
    """
    Configure the merge method for a GitLab project. This determines how merge requests will be processed (merge commit, rebase merge, or fast-forward only).
    
    Args:
        project_id (int): The ID of the GitLab project
        merge_method (str): The merge method to set. Must be one of: 'merge', 'rebase_merge', or 'ff'
    
    Returns:
        Returns the complete project configuration details including the updated merge method and all other project settings."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED', }
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Validate merge_method
    valid_merge_methods = ['merge', 'rebase_merge', 'ff']
    if merge_method not in valid_merge_methods:
        raise ValueError(f"Invalid merge_method. Must be one of: {', '.join(valid_merge_methods)}")
    
    url = f"{base_url}/projects/{project_id}"
    payload = {
        "merge_method": merge_method
    }
    
    response = requests.put(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = set_project_merge_method(project_id=183, merge_method='merge')
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