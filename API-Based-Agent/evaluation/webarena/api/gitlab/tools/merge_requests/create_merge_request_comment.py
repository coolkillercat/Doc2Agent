import requests, json
from urllib.parse import quote

def create_merge_request_comment(merge_request_id: int, body: str, project_id: int = 183, created_at: str = None, 
                                resolved: bool = False, note_type: str = None, position: dict = None):
    """
    Creates a new comment on a specific merge request in GitLab. Useful for providing feedback, starting discussions, 
    or documenting decisions within code review processes.
    
    Args:
        merge_request_id (int): The ID of the merge request to comment on
        body (str): The content of the comment
        project_id (int, optional): The ID of the project containing the merge request. Defaults to 183.
        created_at (str, optional): Date timestamp (ISO 8601) when the comment was created
        resolved (bool, optional): Whether the comment is resolved or not
        note_type (str, optional): The type of the note
        position (dict, optional): Position when creating a diff note
        
    Returns:
        requests.Response: The API response containing the created comment
        
    Example:
        >>> create_merge_request_comment(
        ...     merge_request_id=142596,
        ...     body="This merge request adds the new login functionality",
        ...     created_at="2025-06-12T02:28:28.327Z",
        ...     resolved=True
        ... )
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    
    # Build the API URL for creating a new comment on a merge request
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/projects/{project_id}/merge_requests/{merge_request_id}/notes"
    
    # Prepare the payload with the required and optional parameters
    payload = {
        "body": body
    }
    
    if created_at:
        payload["created_at"] = created_at
    if resolved is not None:
        payload["resolved"] = resolved
    if note_type:
        payload["type"] = note_type
    if position:
        payload["position"] = position
    
    # Make the POST request to create the comment
    response = requests.post(url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    r = create_merge_request_comment(merge_request_id=42, body="This is a test comment on the merge request")
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