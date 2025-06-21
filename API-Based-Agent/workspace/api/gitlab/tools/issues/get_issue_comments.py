import requests, json
from urllib.parse import quote
from typing import List, Dict, Any

def get_issue_comments(issue_id: str) -> requests.Response:
    """
    Retrieves all comments for a specific issue to facilitate discussion tracking and team communication.
    
    Args:
        issue_id (str): The ID of the issue to retrieve comments for
    
    Returns:
        Returns all comments for a specific issue including author details, comment content, and metadata for tracking discussions."""
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Notes API is used for comments as specified in the documentation
    url = f"{base_url}/projects/183/issues/{issue_id}/notes"
    
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    r = get_issue_comments(issue_id="1")  # Assuming issue_id 1 for testing
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