import requests, json
from urllib.parse import quote


def get_epic_notes(group_id, epic_id, sort='desc', order_by='created_at'):
    """
    Retrieves all notes (comments) for a specific epic in a group, with options to control sorting order and sorting field.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group
        epic_id (int): The ID of the epic
        sort (str, optional): Return epic notes sorted in 'asc' or 'desc' order. Default is 'desc'
        order_by (str, optional): Return epic notes ordered by 'created_at' or 'updated_at' fields. Default is 'created_at'
    
    Returns:
        Response: The API response containing the list of epic notes
        
    Example:
        >>> get_epic_notes(group_id="183", epic_id=11)
        >>> get_epic_notes(group_id="my-group", epic_id=42, sort="asc", order_by="updated_at")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct the URL with proper encoding for group_id
    if isinstance(group_id, str) and not group_id.isdigit():
        encoded_group_id = quote(group_id, safe='')
    else:
        encoded_group_id = group_id
    
    url = f"{base_url}/groups/{encoded_group_id}/epics/{epic_id}/notes"
    
    # Add query parameters for sorting and ordering
    params = {
        'sort': sort,
        'order_by': order_by
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response


def get_epic_note(group_id, epic_id, note_id):
    """
    Retrieves a single note for a specific epic in a group.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group
        epic_id (int): The ID of the epic
        note_id (int): The ID of the note
    
    Returns:
        Response: The API response containing the note details
        
    Example:
        >>> get_epic_note(group_id="183", epic_id=11, note_id=302)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct the URL with proper encoding for group_id
    if isinstance(group_id, str) and not group_id.isdigit():
        encoded_group_id = quote(group_id, safe='')
    else:
        encoded_group_id = group_id
    
    url = f"{base_url}/groups/{encoded_group_id}/epics/{epic_id}/notes/{note_id}"
    
    response = requests.get(url, headers=headers)
    return response


def create_epic_note(group_id, epic_id, body, internal=False):
    """
    Creates a new note for a specific epic in a group.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group
        epic_id (int): The ID of the epic
        body (str): The content of the note. Limited to 1,000,000 characters.
        internal (bool, optional): The internal flag of a note. Default is False.
    
    Returns:
        Response: The API response containing the created note details
        
    Example:
        >>> create_epic_note(group_id="183", epic_id=11, body="This is a new note")
        >>> create_epic_note(group_id="183", epic_id=11, body="Internal note", internal=True)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct the URL with proper encoding for group_id
    if isinstance(group_id, str) and not group_id.isdigit():
        encoded_group_id = quote(group_id, safe='')
    else:
        encoded_group_id = group_id
    
    url = f"{base_url}/groups/{encoded_group_id}/epics/{epic_id}/notes"
    
    data = {
        'body': body,
        'internal': internal
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response


def update_epic_note(group_id, epic_id, note_id, body):
    """
    Modifies an existing note of an epic.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group
        epic_id (int): The ID of the epic
        note_id (int): The ID of the note to modify
        body (str): The new content of the note. Limited to 1,000,000 characters.
    
    Returns:
        Response: The API response containing the updated note details
        
    Example:
        >>> update_epic_note(group_id="183", epic_id=11, note_id=302, body="Updated note content")
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct the URL with proper encoding for group_id
    if isinstance(group_id, str) and not group_id.isdigit():
        encoded_group_id = quote(group_id, safe='')
    else:
        encoded_group_id = group_id
    
    url = f"{base_url}/groups/{encoded_group_id}/epics/{epic_id}/notes/{note_id}"
    
    data = {
        'body': body
    }
    
    response = requests.put(url, headers=headers, json=data)
    return response


def delete_epic_note(group_id, epic_id, note_id):
    """
    Deletes an existing note of an epic.
    
    Args:
        group_id (str or int): The ID or URL-encoded path of the group
        epic_id (int): The ID of the epic
        note_id (int): The ID of the note to delete
    
    Returns:
        Response: The API response
        
    Example:
        >>> delete_epic_note(group_id="183", epic_id=11, note_id=302)
    """
    headers = {'Content-Type': 'application/json', 'PRIVATE-TOKEN': 'GITLAB_KEY_REMOVED'}
    
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4"
    
    # Construct the URL with proper encoding for group_id
    if isinstance(group_id, str) and not group_id.isdigit():
        encoded_group_id = quote(group_id, safe='')
    else:
        encoded_group_id = group_id
    
    url = f"{base_url}/groups/{encoded_group_id}/epics/{epic_id}/notes/{note_id}"
    
    response = requests.delete(url, headers=headers)
    return response


if __name__ == '__main__':
    r = get_epic_notes(group_id="183", epic_id=11, sort="desc", order_by="created_at")
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