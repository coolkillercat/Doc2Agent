import requests

def redaction(node_id=None, version=None, redaction_id=None):
    """
    Redacts a specific version of an OSM element (node, way, or relation).
    
    This API method was originally created for the ODbL license change to hide 
    contributions from users that did not accept the new CT/licence. It is now 
    used by the DWG to hide old versions of elements containing data privacy or 
    copyright infringements.
    
    Args:
        node_id (int): The ID of the element to redact.
        version (int): The version of the element to redact.
        redaction_id (int): The ID of the redaction to use.
        
    Returns:
        requests.Response: The response from the API.
        
    Example:
        >>> redaction(node_id=123, version=1, redaction_id=456)
    """
    assert node_id is not None, 'Missing required parameter: node_id'
    assert version is not None, 'Missing required parameter: version'
    assert redaction_id is not None, 'Missing required parameter: redaction_id'
    
    # Determine element type (node, way, or relation)
    # For simplicity, we'll assume it's a node if not specified
    element_type = "node"
    
    api_url = f"https://api.openstreetmap.org/api/0.6/{element_type}/{node_id}/{version}/redact?redaction={redaction_id}"
    
    response = requests.post(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = redaction(node_id=123, version=1, redaction_id=456)
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