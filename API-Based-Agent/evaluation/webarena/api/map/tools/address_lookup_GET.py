import requests, json
from urllib.parse import quote


def address_lookup(osm_ids=None, format='jsonv2', json_callback=None, addressdetails=None, extratags=None, namedetails=None, accept_language=None, polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None, email=None, debug=None):
    """
    Query the address and other details of one or multiple OSM objects using Nominatim's lookup API.
    
    Parameters:
    -----------
    osm_ids : str
        Comma-separated list of OSM ids each prefixed with its type (N for node, W for way, R for relation).
        Up to 50 ids can be queried at the same time. Required parameter.
        Example: "R146656,W104393803,N240109189"
    
    format : str, optional
        Output format. One of: 'xml', 'json', 'jsonv2', 'geojson', 'geocodejson'. Default is 'jsonv2'.
    
    json_callback : str, optional
        Function name for JSONP callback. Only has an effect for JSON output formats.
    
    addressdetails : int, optional
        When set to 1, include a breakdown of the address into elements.
    
    extratags : int, optional
        When set to 1, include any additional information available in the database.
    
    namedetails : int, optional
        When set to 1, include a full list of names for the result.
    
    accept_language : str, optional
        Preferred language order for showing search results.
        Example: "en-US,en;q=0.5"
    
    polygon_geojson : int, optional
        When set to 1, add the full geometry of the place in GeoJSON format.
    
    polygon_kml : int, optional
        When set to 1, add the full geometry of the place in KML format.
    
    polygon_svg : int, optional
        When set to 1, add the full geometry of the place in SVG format.
    
    polygon_text : int, optional
        When set to 1, add the full geometry of the place in WKT format.
    
    polygon_threshold : float, optional
        When one of the polygon_* outputs is chosen, return a simplified version of the output geometry.
    
    email : str, optional
        Valid email address to identify your requests if making large numbers of requests.
    
    debug : int, optional
        When set to 1, output assorted developer debug information.
    
    Returns:
    --------
    requests.Response
        The response from the API.
    
    Example:
    --------
    >>> response = address_lookup(
    ...     osm_ids="R146656,W104393803,N240109189",
    ...     format="json",
    ...     addressdetails=1,
    ...     extratags=1
    ... )
    >>> print(response.status_code)
    200
    """
    api_url = "https://nominatim.openstreetmap.org/lookup"
    
    if osm_ids is None:
        osm_ids = "R146656,W104393803,N240109189"  # Default value if not provided
    
    # Remove None values from querystring
    querystring = {k: v for k, v in {
        'osm_ids': osm_ids,
        'format': format,
        'json_callback': json_callback,
        'addressdetails': addressdetails,
        'extratags': extratags,
        'namedetails': namedetails,
        'accept-language': accept_language,
        'polygon_geojson': polygon_geojson,
        'polygon_kml': polygon_kml,
        'polygon_svg': polygon_svg,
        'polygon_text': polygon_text,
        'polygon_threshold': polygon_threshold,
        'email': email,
        'debug': debug
    }.items() if v is not None}
    
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = address_lookup(osm_ids='R146656', format='json', json_callback='myCallbackFunction', addressdetails=1, extratags=1, namedetails=1, accept_language='en-US,en;q=0.5', polygon_geojson=1, polygon_threshold=0.01, email='user@example.com')
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