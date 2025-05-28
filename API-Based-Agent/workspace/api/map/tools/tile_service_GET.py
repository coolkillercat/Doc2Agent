import requests
from urllib.parse import quote

def tile_service(x=None, y=None, zoom=None):
    """
    Fetches a vector tile from the OSRM tile service.
    
    This function retrieves a Mapbox Vector Tile (MVT) from the OSRM tile service
    for the specified tile coordinates. The tiles contain road geometries and metadata
    that can be used to examine the routing graph.
    
    Args:
        x (int): The x coordinate of the tile. Required.
        y (int): The y coordinate of the tile. Required.
        zoom (int): The zoom level of the tile. Required. Must be >= 12.
    
    Returns:
        requests.Response: The HTTP response containing the vector tile data.
        The response object has a binary encoded blob with a Content-Type of 
        application/x-protobuf, or a 404 error if the tile is not found.
    
    Example:
        # Fetch a Z=13 tile for downtown San Francisco
        response = tile_service(x=1310, y=3166, zoom=13)
    """
    assert x is not None, 'Missing required parameter: x'
    assert y is not None, 'Missing required parameter: y'
    assert zoom is not None, 'Missing required parameter: zoom'
    
    api_url = f"http://router.project-osrm.org/tile/v1/test/tile({x},{y},{zoom}).mvt"
    
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response = requests.get(url=api_url, timeout=50)  # in case API can't handle redundant params
    return response

if __name__ == '__main__':
    r = tile_service(x=1310, y=3166, zoom=13)
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
    result_dict['content'] = r.content.decode("utf-8", errors="replace")
    print(json.dumps(result_dict, indent=4))
