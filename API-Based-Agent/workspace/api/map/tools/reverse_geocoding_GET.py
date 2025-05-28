import requests, json
from urllib.parse import quote


def reverse_geocoding(lat=None, lon=None, format='xml', json_callback=None, addressdetails=1, extratags=None, namedetails=None, accept_language=None, zoom=18, layer=None, polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None):
    """
    Reverse geocoding generates an address from a coordinate given as latitude and longitude.
    
    Parameters:
    -----------
    lat : float
        Latitude of the coordinate in WGS84 projection.
    lon : float
        Longitude of the coordinate in WGS84 projection.
    format : str, optional
        Output format. One of: 'xml', 'json', 'jsonv2', 'geojson', 'geocodejson'. Default is 'xml'.
    json_callback : str, optional
        Function name for JSONP callback. Only has an effect for JSON output formats.
    addressdetails : int, optional
        When set to 1, include a breakdown of the address into elements. Default is 1.
    extratags : int, optional
        When set to 1, include any additional information available in the database. Default is None.
    namedetails : int, optional
        When set to 1, include a full list of names for the result. Default is None.
    accept_language : str, optional
        Preferred language order for showing search results. Default is None.
    zoom : int, optional
        Level of detail required for the address (0-18). Default is 18.
    layer : str, optional
        Comma-separated list of: 'address', 'poi', 'railway', 'natural', 'manmade'. Default is None.
    polygon_geojson : int, optional
        Add the full geometry of the place to the result output in GeoJSON format. Default is None.
    polygon_kml : int, optional
        Add the full geometry of the place to the result output in KML format. Default is None.
    polygon_svg : int, optional
        Add the full geometry of the place to the result output in SVG format. Default is None.
    polygon_text : int, optional
        Add the full geometry of the place to the result output in WKT format. Default is None.
    polygon_threshold : float, optional
        When one of the polygon_* outputs is chosen, return a simplified version of the output geometry. Default is None.
    
    Returns:
    --------
    requests.Response
        The response from the API.
    
    Examples:
    ---------
    >>> reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987, format='json')
    >>> reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987, format='jsonv2', addressdetails=1, extratags=1)
    >>> reverse_geocoding(lat=44.50155, lon=11.33989, format='geojson', zoom=15)
    """
    api_url = "https://nominatim.openstreetmap.org/reverse"
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0'
    }
    
    # Remove None values from querystring
    querystring = {k: v for k, v in {
        'lat': lat, 
        'lon': lon, 
        'format': format, 
        'json_callback': json_callback, 
        'addressdetails': addressdetails, 
        'extratags': extratags, 
        'namedetails': namedetails, 
        'accept-language': accept_language, 
        'zoom': zoom, 
        'layer': layer, 
        'polygon_geojson': polygon_geojson, 
        'polygon_kml': polygon_kml, 
        'polygon_svg': polygon_svg, 
        'polygon_text': polygon_text, 
        'polygon_threshold': polygon_threshold
    }.items() if v is not None}
    
    assert lat is not None, 'Missing required parameter: lat'
    assert lon is not None, 'Missing required parameter: lon'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50)
    return response

if __name__ == '__main__':
    r = reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987, format='json', json_callback='myCallback', addressdetails=1, extratags=1, namedetails=1, accept_language='en-US,fr', zoom=10, layer='address,poi', polygon_geojson=1)
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