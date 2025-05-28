import requests, json
from urllib.parse import quote

def ways_for_node(node_id=None):
    """
    Retrieves all ways that contain the specified node.
    
    This function queries the OpenStreetMap API to find all ways that reference
    the given node ID.
    
    Args:
        node_id (int or str): The ID of the node to query. Required.
        
    Returns:
        requests.Response: The API response object containing the ways data.
        
    Example:
        >>> response = ways_for_node(123)
        >>> print(response.status_code)  # 200 if successful
        >>> print(response.text)  # XML content with ways data
    """
    assert node_id is not None, 'Missing required parameter: node_id'
    
    # Format the URL correctly - replace #id with the actual node_id
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000/api/0.6/node/{node_id}/ways"
    
    # No need for querystring parameters as the node_id is part of the URL path
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = ways_for_node(node_id=123)
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