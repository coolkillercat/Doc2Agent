import requests, json
from urllib.parse import quote


def create_subgroup(parent_id: int, subgroup_path: str, subgroup_name: str, description: str = None, visibility: str = None) -> dict:
    """
    Creates a new subgroup under a parent group in GitLab. The parent_id specifies the parent group, 
    while subgroup_path and subgroup_name define the URL path and display name for the new subgroup.
    
    Args:
        parent_id (int): The ID of the parent group
        subgroup_path (str): The path for the new subgroup (used in URLs)
        subgroup_name (str): The display name for the new subgroup
        description (str, optional): Description for the subgroup
        visibility (str, optional): Visibility level of the subgroup (private, internal, or public)
        
    Returns:
        dict: The API response as a dictionary
        
    Example:
        >>> create_subgroup(parent_id=183, subgroup_path="test-subgroup", subgroup_name="Test Subgroup")
        >>> create_subgroup(parent_id=183, subgroup_path="dev-team", subgroup_name="Development Team", description="Team for developers", visibility="private")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/"
    
    data = {
        "path": subgroup_path,
        "name": subgroup_name,
        "parent_id": parent_id
    }
    
    if description:
        data["description"] = description
    
    if visibility:
        data["visibility"] = visibility
    
    response = requests.post(url, headers=headers, json=data)
    return response


if __name__ == '__main__':
    r = create_subgroup(parent_id=183, subgroup_path="test-subgroup", subgroup_name="Test Subgroup")
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