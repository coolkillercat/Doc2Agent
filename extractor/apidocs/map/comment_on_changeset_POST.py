import requests

def comment_on_changeset(changeset_id, text=None):
    """
    Add a comment to a changeset.
    
    This function adds a comment to a specified changeset. The changeset must be closed.
    
    Args:
        changeset_id (int): The ID of the changeset to comment on.
        text (str, optional): The comment text. Cannot be empty.
        
    Returns:
        requests.Response: The response from the API.
        
    Raises:
        AssertionError: If the text parameter is None or empty.
        
    Examples:
        >>> comment_on_changeset(12345, "This is a comment.")
        <Response [200]>
    """
    assert text is not None, 'Missing required parameter: text'
    assert text.strip() != '', 'Text parameter cannot be empty'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/changeset/{changeset_id}/comment"
    
    # The API expects form data, not JSON
    payload = {'text': text}
    
    response = requests.post(url=api_url, data=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = comment_on_changeset(12345, text='This is a comment.')
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