import requests, json
from urllib.parse import quote


def route_service(coordinates=None, alternatives=None, steps=None, geometries=None, overview=None, annotations=None):
    """
    Find the fastest route between coordinates in the supplied order.
    
    Parameters:
    -----------
    coordinates : str
        String of format `{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]` or `polyline({polyline}) or polyline6({polyline6})`.
        Example: "13.388860,52.517037;13.397634,52.529407;13.428555,52.523219"
    alternatives : str
        Search for alternative routes. Values: "true", "false" (default), or a number.
        Example: "true"
    steps : str
        Returned route steps for each route leg. Values: "true", "false" (default).
        Example: "false"
    geometries : str
        Returned route geometry format. Values: "polyline" (default), "polyline6", "geojson".
        Example: "geojson"
    overview : str
        Add overview geometry. Values: "simplified" (default), "full", "false".
        Example: "simplified"
    annotations : str
        Returns additional metadata for each coordinate. Values: "true", "false" (default), "nodes", "distance", "duration", "datasources", "weight", "speed".
        Example: "true"
    
    Returns:
    --------
    response : requests.Response
        The HTTP response from the OSRM API.
    """
    base_url = "http://router.project-osrm.org/route/v1/test/"
    
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    # Build query parameters
    params = {}
    if alternatives is not None:
        params['alternatives'] = alternatives
    if steps is not None:
        params['steps'] = steps
    if geometries is not None:
        params['geometries'] = geometries
    if overview is not None:
        params['overview'] = overview
    if annotations is not None:
        params['annotations'] = annotations
    
    # Construct the URL
    url = f"{base_url}{quote(coordinates, safe='')}"
    
    # Make the request
    response = requests.get(url=url, params=params, timeout=50)
    return response

if __name__ == '__main__':
    r = route_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219', alternatives='true', steps='false', geometries='geojson', overview='simplified', annotations='true')
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
