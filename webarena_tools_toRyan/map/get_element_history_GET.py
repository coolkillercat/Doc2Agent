import requests

def get_element_history(id=None, element_type='way'):
    """
    Retrieves the history of an OSM element (node, way, or relation).
    
    Parameters:
    -----------
    id : int
        The ID of the element to retrieve history for.
    element_type : str, optional
        The type of element ('node', 'way', or 'relation'). Default is 'way'.
    
    Returns:
    --------
    requests.Response
        The response object from the API request.
    
    Examples:
    ---------
    >>> response = get_element_history(id=250066046, element_type='way')
    >>> response = get_element_history(id=123456, element_type='node')
    >>> response = get_element_history(id=789012, element_type='relation')
    """
    assert id is not None, 'Missing required parameter: id'
    assert element_type in ['node', 'way', 'relation'], 'element_type must be one of: node, way, relation'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/{element_type}/{id}/history"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = get_element_history(id=250066046)
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