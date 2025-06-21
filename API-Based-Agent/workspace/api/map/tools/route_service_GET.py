import requests, json
from urllib.parse import quote


def route_service(coordinates=None, alternatives='false', steps='false', geometries='polyline', overview='simplified', annotations='false', profile='5000'):
    """
    Find the fastest route between coordinates in the supplied order.
    
    Parameters:
    -----------
    coordinates : str
        String of format `{longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...]` or 
        `polyline({polyline})` or `polyline6({polyline6})`.
        Example: '13.388860,52.517037;13.397634,52.529407;13.428555,52.523219'
    
    alternatives : str, optional
        Search for alternative routes. Can be 'true', 'false', or a number.
        Default is 'false'.
    
    steps : str, optional
        Return route steps for each route leg. Can be 'true' or 'false'.
        Default is 'false'.
    
    geometries : str, optional
        Returned route geometry format. Can be 'polyline', 'polyline6', or 'geojson'.
        Default is 'polyline'.
    
    overview : str, optional
        Add overview geometry. Can be 'simplified', 'full', or 'false'.
        Default is 'simplified'.
    
    annotations : str, optional
        Returns additional metadata. Can be 'true', 'false', 'nodes', 'distance', 'duration', 'datasources', 'weight', or 'speed'.
        Default is 'false'.
    
    profile : str, optional
        Mode of transportation. Can be '5000' for car, '5001' for bicycle, or '5002' for foot.
        Default is '5000'.
    
    Returns:
    --------
    response : requests.Response
        The HTTP response from the OSRM API.
    
    Examples:
    ---------
    >>> route_service(coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219')
    >>> route_service(coordinates='13.388860,52.517037;13.397634,52.529407', alternatives='true', steps='true', geometries='geojson', overview='full', annotations='true')
    """
    base_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com"
    api_url = f"{base_url}:{profile}/route/v1/test/{coordinates}"
    
    querystring = {
        'alternatives': alternatives,
        'steps': steps,
        'geometries': geometries,
        'overview': overview,
        'annotations': annotations
    }
    
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    r = route_service(
        coordinates='13.388860,52.517037;13.397634,52.529407;13.428555,52.523219',
        alternatives='true',
        steps='true',
        geometries='geojson',
        overview='full',
        annotations='true'
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