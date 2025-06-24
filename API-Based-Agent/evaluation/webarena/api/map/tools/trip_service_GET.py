import requests, json
from urllib.parse import quote


def trip_service(coordinates=None, roundtrip=True, source='any', destination='any', steps=False, geometries='polyline', overview='simplified', annotations=False, profile=5000):
    """
    The trip plugin solves the Traveling Salesman Problem using a greedy heuristic for 10 or more waypoints
    and uses brute force for less than 10 waypoints. The returned path does not have to be the fastest one.
    
    Parameters:
    -----------
    coordinates : str
        String of format `{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]`.
        Example: '13.388860,52.517037;13.397634,52.529407;13.428555,52.523219'
    roundtrip : bool, default=True
        Returned route is a roundtrip (route returns to first location)
    source : str, default='any'
        Returned route starts at 'any' or 'first' coordinate
    destination : str, default='any'
        Returned route ends at 'any' or 'last' coordinate
    steps : bool, default=False
        Returned route instructions for each trip
    geometries : str, default='polyline'
        Returned route geometry format. One of 'polyline', 'polyline6', 'geojson'
    overview : str, default='simplified'
        Add overview geometry either 'full', 'simplified', or 'false'
    annotations : bool or str, default=False
        Returns additional metadata for each coordinate along the route geometry
    profile : int, default=5000
        Mode of transportation. 5000 for car, 5001 for bicycle, 5002 for foot
    
    Returns:
    --------
    response : requests.Response
        Response from the OSRM API
    
    Examples:
    ---------
    >>> trip_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219')
    >>> trip_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219', 
    ...              roundtrip=False, source='first', destination='last')
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com"
    api_url = f"{base_url}:{profile}/trip/v1/test/{coordinates}"
    
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    # Convert boolean values to strings
    roundtrip_str = str(roundtrip).lower()
    steps_str = str(steps).lower()
    annotations_str = str(annotations).lower() if isinstance(annotations, bool) else annotations
    
    querystring = {
        'roundtrip': roundtrip_str,
        'source': source,
        'destination': destination,
        'steps': steps_str,
        'geometries': geometries,
        'overview': overview,
        'annotations': annotations_str
    }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = trip_service(
        coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219',
        roundtrip=False,
        source='first',
        destination='last',
        steps=True,
        geometries='geojson',
        overview='full',
        annotations=True
    )
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