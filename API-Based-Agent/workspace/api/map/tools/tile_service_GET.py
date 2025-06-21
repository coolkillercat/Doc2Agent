import requests
from urllib.parse import quote

def tile_service(x=None, y=None, zoom=None, profile=5000):
    """
    Fetch a vector tile from the OSRM tile service.
    
    This function retrieves a Mapbox Vector Tile (MVT) from the OSRM backend service
    for the specified tile coordinates and zoom level.
    
    Parameters:
    -----------
    x : int
        The x coordinate of the tile. Required.
    y : int
        The y coordinate of the tile. Required.
    zoom : int
        The zoom level of the tile. Required.
    profile : int, optional
        Mode of transportation. One of the following values:
        - 5000 for car (driving)
        - 5001 for bicycle (biking)
        - 5002 for foot (walking)
        Default is 5000 (car).
    
    Returns:
    --------
    requests.Response
        The HTTP response object containing the MVT data.
    
    Examples:
    ---------
    >>> response = tile_service(x=1310, y=3166, zoom=13)
    >>> response.status_code
    200
    """
    assert x is not None, 'Missing required parameter: x'
    assert y is not None, 'Missing required parameter: y'
    assert zoom is not None, 'Missing required parameter: zoom'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:{profile}/tile/v1/test/tile({x},{y},{zoom}).mvt"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
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