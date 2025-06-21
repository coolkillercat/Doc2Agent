import requests

def match_service(profile=None, coordinates=None, steps=None, geometries='polyline', overview='simplified', annotations=None, timestamps=None, radiuses=None):
    """
    Map matching matches/snaps given GPS points to the road network in the most plausible way.
    
    Parameters:
    -----------
    profile : str
        Mode of transportation, typically 'car', 'bike' or 'foot'.
        Example: 'driving'
    
    coordinates : str
        String of format '{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]'
        Example: '13.388860,52.517037;13.397634,52.529407;13.428555,52.523219'
    
    steps : bool, optional
        Return route steps for each route. Default is False.
    
    geometries : str, optional
        Returned route geometry format. One of 'polyline', 'polyline6', 'geojson'. Default is 'polyline'.
    
    overview : str, optional
        Add overview geometry either 'simplified', 'full', or 'false'. Default is 'simplified'.
    
    annotations : bool, optional
        Returns additional metadata for each coordinate along the route geometry. Default is False.
    
    timestamps : str, optional
        Timestamps for the input locations in seconds since UNIX epoch.
        Example: '1609459200;1609459260;1609459320'
    
    radiuses : str, optional
        Standard deviation of GPS precision used for map matching.
        Example: '10;15;20'
    
    Returns:
    --------
    response : requests.Response
        The HTTP response from the OSRM API.
    """
    assert profile is not None, 'Missing required parameter: profile'
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    base_url = f"http://router.project-osrm.org/match/v1/{profile}/{coordinates}"
    
    params = {}
    if steps is not None:
        params['steps'] = 'true' if steps else 'false'
    if geometries is not None:
        params['geometries'] = geometries
    if overview is not None:
        params['overview'] = overview
    if annotations is not None:
        params['annotations'] = 'true' if annotations else 'false'
    if timestamps is not None:
        params['timestamps'] = timestamps
    if radiuses is not None:
        params['radiuses'] = radiuses
    
    response = requests.get(url=base_url, params=params)
    return response