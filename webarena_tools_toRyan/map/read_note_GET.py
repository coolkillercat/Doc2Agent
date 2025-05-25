import requests, json
from urllib.parse import quote


def read_note(id=None):
    """
    Retrieve a note by its ID from the OpenStreetMap API.
    
    Parameters:
    -----------
    id : int
        The ID of the note to retrieve. This parameter is required.
        
    Returns:
    --------
    requests.Response
        The response object from the API request.
        
    Examples:
    ---------
    >>> read_note(id=100)
    <Response [200]>
    """
    assert id is not None, 'Missing required parameter: id'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/notes/{id}"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = read_note(id=100)
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