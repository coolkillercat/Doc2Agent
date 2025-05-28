import requests, json
from urllib.parse import quote


def match_service(coordinates=None, steps=None, geometries=None, overview=None, annotations=None):
    """
    Map matching matches/snaps given GPS points to the road network in the most plausible way.
    
    Parameters:
    -----------
    coordinates : str
        String of format `{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]`.
        Example: "13.388860,52.517037;13.397634,52.529407;13.428555,52.523219"
    steps : bool, optional
        Returned route steps for each route. Default is False.
    geometries : str, optional
        Returned route geometry format. One of "polyline" (default), "polyline6", "geojson".
    overview : str, optional
        Add overview geometry either "simplified" (default), "full", or "false".
    annotations : bool or str, optional
        Returns additional metadata for each coordinate along the route geometry.
        Can be True, False (default), "nodes", "distance", "duration", "datasources", "weight", "speed".
    
    Returns:
    --------
    requests.Response
        The response from the OSRM API.
    
    Example:
    --------
    >>> match_service(coordinates="13.388860,52.517037;13.397634,52.529407;13.428555,52.523219", 
    ...               steps=True, 
    ...               geometries="geojson", 
    ...               overview="simplified", 
    ...               annotations=True)
    """
    base_url = "http://router.project-osrm.org/match/v1/test/"
    
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    # Convert boolean parameters to lowercase strings
    if steps is not None:
        steps = str(steps).lower()
    if annotations is not None and isinstance(annotations, bool):
        annotations = str(annotations).lower()
    
    querystring = {}
    if steps is not None:
        querystring['steps'] = steps
    if geometries is not None:
        querystring['geometries'] = geometries
    if overview is not None:
        querystring['overview'] = overview
    if annotations is not None:
        querystring['annotations'] = annotations
    
    api_url = f"{base_url}{quote(coordinates, safe='')}"
    
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50)  # in case API can't handle redundant params
        response = response2
    return response

if __name__ == '__main__':
    r = match_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219', steps=False, geometries='geojson', overview='simplified', annotations=True)
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
