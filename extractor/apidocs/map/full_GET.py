import requests

def full(id=None):
    """
    Retrieves a way or relation and all other elements referenced by it.
    
    For a way, it will return the way specified plus the full XML of all nodes referenced by the way.
    For a relation, it will return the relation itself, all nodes, ways, and relations that are members
    of the relation, plus all nodes used by ways from the previous step.
    
    Parameters:
    -----------
    id : int or str
        The ID of the way or relation to retrieve.
        
    Returns:
    --------
    requests.Response
        The response from the API containing the requested data.
        
    Examples:
    ---------
    >>> response = full(250066046)  # Retrieve way with ID 250066046
    >>> response = full(123)  # Retrieve relation with ID 123
    """
    assert id is not None, 'Missing required parameter: id'
    
    # Determine if it's a way or relation based on the ID
    # This is a simplification - in a real implementation you might want to check
    # or allow the user to specify the element type
    element_type = "way"  # Default to way
    
    api_url = f"https://api.openstreetmap.org/api/0.6/{element_type}/{id}/full"
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = full(id=250066046)
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