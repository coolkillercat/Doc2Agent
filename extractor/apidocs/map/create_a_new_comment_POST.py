import requests

def create_a_new_comment(id=None, text=None):
    """
    Add a new comment to a note.
    
    Parameters:
    -----------
    id : int
        The ID of the note to comment on. Required.
    text : str
        The comment text. Required.
        
    Returns:
    --------
    requests.Response
        The response from the API.
        
    Examples:
    ---------
    >>> create_a_new_comment(id=16659, text='This is a comment')
    """
    assert id is not None, 'Missing required parameter: id'
    assert text is not None, 'Missing required parameter: text'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/notes/{id}/comment"
    payload = {'text': text}
    
    response = requests.post(url=api_url, data=payload, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = create_a_new_comment(id=16659, text='This is a comment')
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