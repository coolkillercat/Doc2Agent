import requests

def read_changeset(id=None, include_discussion=None):
    """
    Retrieves information about a specific changeset from the OpenStreetMap API.
    
    Parameters:
    -----------
    id : int
        The ID of the changeset to retrieve. Required.
    include_discussion : bool
        If True, the result will include the changeset discussion. 
        If False or None, the discussion will not be included.
    
    Returns:
    --------
    requests.Response
        The API response containing changeset information.
    
    Examples:
    ---------
    >>> response = read_changeset(id=12345)
    >>> response = read_changeset(id=12345, include_discussion=True)
    """
    assert id is not None, 'Missing required parameter: id'
    
    # Construct the URL with the ID directly in the path
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/changeset/{id}"
    
    # Add include_discussion as a query parameter if provided
    params = {}
    if include_discussion:
        params['include_discussion'] = 'true'
    
    response = requests.get(url=api_url, params=params, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = read_changeset(id=12345, include_discussion=True)
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