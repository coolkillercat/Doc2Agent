import requests, json
from urllib.parse import quote


def trip_service(coordinates=None, roundtrip=None, source=None, destination=None, steps=None, geometries=None, overview=None, annotations=None):
    """
    Solves the Traveling Salesman Problem using a greedy heuristic for 10 or more waypoints and brute force for less than 10 waypoints.
    
    Parameters:
    -----------
    coordinates : str
        String of format `{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]`.
        Example: '13.388860,52.517037;13.397634,52.529407;13.428555,52.523219'
    roundtrip : bool
        Returned route is a roundtrip (route returns to first location). Default is True.
    source : str
        Returned route starts at 'any' or 'first' coordinate. Default is 'any'.
    destination : str
        Returned route ends at 'any' or 'last' coordinate. Default is 'any'.
    steps : bool
        Returned route instructions for each trip. Default is False.
    geometries : str
        Returned route geometry format. Options: 'polyline', 'polyline6', 'geojson'. Default is 'polyline'.
    overview : str
        Add overview geometry. Options: 'simplified', 'full', 'false'. Default is 'simplified'.
    annotations : bool or str
        Returns additional metadata for each coordinate along the route geometry.
        Options: True, False, 'nodes', 'distance', 'duration', 'datasources', 'weight', 'speed'. Default is False.
    
    Returns:
    --------
    response : requests.Response
        The HTTP response from the OSRM API.
    
    Example:
    --------
    >>> trip_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219', 
    ...              roundtrip=True, 
    ...              source='first', 
    ...              destination='last', 
    ...              geometries='geojson')
    """
    base_url = "http://router.project-osrm.org/trip/v1/test/"
    
    # Build the URL with the coordinates
    api_url = f"{base_url}{quote(coordinates, safe='')}"
    
    # Prepare query parameters
    querystring = {}
    if roundtrip is not None:
        querystring['roundtrip'] = str(roundtrip).lower()
    if source is not None:
        querystring['source'] = source
    if destination is not None:
        querystring['destination'] = destination
    if steps is not None:
        querystring['steps'] = str(steps).lower()
    if geometries is not None:
        querystring['geometries'] = geometries
    if overview is not None:
        querystring['overview'] = overview
    if annotations is not None:
        if isinstance(annotations, bool):
            querystring['annotations'] = str(annotations).lower()
        else:
            querystring['annotations'] = annotations
    
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    response = requests.get(url=api_url, params=querystring, timeout=50)
    return response

if __name__ == '__main__':
    r = trip_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219', 
                     roundtrip=True, 
                     source='first', 
                     destination='last', 
                     steps=False, 
                     geometries='geojson', 
                     overview='simplified', 
                     annotations=True)
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
