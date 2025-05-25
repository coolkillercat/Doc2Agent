import requests, json
from urllib.parse import quote

def relations_for_element(element_id=None, element_type=None):
    """
    Retrieves all (not deleted) relations in which the given element is used.
    
    Parameters:
    -----------
    element_id : str or int
        The ID of the element to retrieve relations for.
    element_type : str
        The type of element ('node', 'way', or 'relation').
        
    Returns:
    --------
    requests.Response
        The response from the API containing relations data.
        
    Examples:
    ---------
    >>> relations_for_element(element_id=123, element_type='node')
    >>> relations_for_element(element_id=456, element_type='way')
    >>> relations_for_element(element_id=789, element_type='relation')
    """
    assert element_id is not None, 'Missing required parameter: element_id'
    assert element_type is not None, 'Missing required parameter: element_type'
    assert element_type in ['node', 'way', 'relation'], 'element_type must be one of: node, way, relation'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/{element_type}/{element_id}/relations"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = relations_for_element(element_id=123, element_type='node')
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