import requests, json
from urllib.parse import quote

def mark_todo_as_done(todo_id: int) -> dict:
    """
    Marks a specific to-do item as completed based on its ID. Returns the completed to-do item with all its details including associated project, author, and target information.
    
    Args:
        todo_id (int): The ID of the to-do item to mark as done
    
    Returns:
        dict: The API response containing details of the marked to-do item
        
    Example:
        >>> result = mark_todo_as_done(todo_id=102)
        >>> print(result['state'])
        'done'
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'glpat-qvQ-N6mN_tAddXb2WWdi'}
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    url = f"{base_url}/todos/{todo_id}/mark_as_done"
    
    response = requests.post(url, headers=headers)
    return response.json() if response.content else {}

if __name__ == '__main__':
    r = mark_todo_as_done(todo_id=102)
    r_json = r
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))