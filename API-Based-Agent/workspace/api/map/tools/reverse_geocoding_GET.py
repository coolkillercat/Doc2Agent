import requests, json
from urllib.parse import quote


def reverse_geocoding(lat=None, lon=None, format='jsonv2', json_callback=None, addressdetails=1, extratags=0, namedetails=0, accept_language=None, zoom=18, layer=None, polygon_geojson=0, polygon_threshold=0.0, email=None, debug=0):
    """
    Reverse geocoding generates an address from a coordinate given as latitude and longitude.
    
    Parameters:
    -----------
    lat : float
        Latitude of the coordinate in WGS84 projection.
    lon : float
        Longitude of the coordinate in WGS84 projection.
    format : str, optional
        Output format. One of: 'xml', 'json', 'jsonv2', 'geojson', 'geocodejson'. Default is 'jsonv2'.
    json_callback : str, optional
        Function name for JSONP callback. Only has an effect for JSON output formats.
    addressdetails : int, optional
        Include a breakdown of the address into elements (0 or 1). Default is 1.
    extratags : int, optional
        Include additional information in the result (0 or 1). Default is 0.
    namedetails : int, optional
        Include a full list of names for the result (0 or 1). Default is 0.
    accept_language : str, optional
        Preferred language order for showing search results.
    zoom : int, optional
        Level of detail required for the address (0-18). Default is 18.
    layer : str, optional
        Filter places by themes. Comma-separated list of: 'address', 'poi', 'railway', 'natural', 'manmade'.
    polygon_geojson : int, optional
        Add the full geometry of the place to the result in GeoJSON format (0 or 1). Default is 0.
    polygon_threshold : float, optional
        Simplify the output geometry with the given tolerance. Default is 0.0.
    email : str, optional
        Valid email address to identify your requests.
    debug : int, optional
        Output developer debug information (0 or 1). Default is 0.
    
    Returns:
    --------
    dict or str
        The parsed response from the Nominatim API based on the format requested.
    
    Examples:
    ---------
    >>> reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987)
    >>> reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987, format='jsonv2', addressdetails=1)
    >>> reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987, format='geojson', json_callback='myCallbackFunction', addressdetails=1, extratags=1, namedetails=1, accept_language='en-US', zoom=10, layer='address,poi', polygon_geojson=1, polygon_threshold=0.01, email='user@example.com')
    """
    api_url = "https://nominatim.openstreetmap.org/reverse"
    
    assert lat is not None, 'Missing required parameter: lat'
    assert lon is not None, 'Missing required parameter: lon'
    
    querystring = {
        'lat': lat,
        'lon': lon,
        'format': format
    }
    
    # Add optional parameters only if they are provided
    if json_callback is not None:
        querystring['json_callback'] = json_callback
    if addressdetails is not None:
        querystring['addressdetails'] = addressdetails
    if extratags is not None:
        querystring['extratags'] = extratags
    if namedetails is not None:
        querystring['namedetails'] = namedetails
    if accept_language is not None:
        querystring['accept-language'] = accept_language
    if zoom is not None:
        querystring['zoom'] = zoom
    if layer is not None:
        querystring['layer'] = layer
    if polygon_geojson is not None:
        querystring['polygon_geojson'] = polygon_geojson
    if polygon_threshold is not None:
        querystring['polygon_threshold'] = polygon_threshold
    if email is not None:
        querystring['email'] = email
    if debug is not None:
        querystring['debug'] = debug
    
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    
    if debug == 1:
        return response.text
    
    if format in ['json', 'jsonv2', 'geojson', 'geocodejson']:
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
    else:
        return response.text

if __name__ == '__main__':
    result = reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987, format='jsonv2')
    print(json.dumps(result, indent=4))