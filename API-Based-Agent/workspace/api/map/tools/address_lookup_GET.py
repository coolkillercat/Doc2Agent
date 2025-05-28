import requests, json
from urllib.parse import quote


def address_lookup(osm_ids=None, format='jsonv2', json_callback=None, addressdetails=None, extratags=None, namedetails=None, accept_language=None, polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None):
    """
    Query the address and other details of one or multiple OSM objects like node, way or relation.
    
    Parameters:
    -----------
    osm_ids : str
        Comma-separated list of OSM ids each prefixed with its type, one of node(N), way(W) or relation(R).
        Up to 50 ids can be queried at the same time. Required parameter.
        Example: "W50637691,N240109189,R146656"
    
    format : str, optional
        Output format. One of: 'xml', 'json', 'jsonv2', 'geojson', 'geocodejson'. Default is 'jsonv2'.
    
    json_callback : str, optional
        Function name for JSONP callback. Only has an effect for JSON output formats.
        Example: "myCallbackFunction"
    
    addressdetails : int, optional
        When set to 1, include a breakdown of the address into elements. Default is 0.
    
    extratags : int, optional
        When set to 1, include additional information available in the database. Default is 0.
    
    namedetails : int, optional
        When set to 1, include a full list of names for the result. Default is 0.
    
    accept_language : str, optional
        Preferred language order for showing search results.
        Example: "en-US,fr"
    
    polygon_geojson : int, optional
        Add the full geometry of the place to the result in GeoJSON format. Default is 0.
    
    polygon_kml : int, optional
        Add the full geometry of the place to the result in KML format. Default is 0.
    
    polygon_svg : int, optional
        Add the full geometry of the place to the result in SVG format. Default is 0.
    
    polygon_text : int, optional
        Add the full geometry of the place to the result in WKT format. Default is 0.
    
    polygon_threshold : float, optional
        When one of the polygon_* outputs is chosen, return a simplified version of the output geometry.
        The parameter describes the tolerance in degrees. Default is 0.0.
    
    Returns:
    --------
    requests.Response
        The response from the API.
    
    Examples:
    ---------
    >>> r = address_lookup(osm_ids="W50637691,N240109189", format="json", extratags=1)
    >>> r = address_lookup(osm_ids="R146656,W50637691,N240109189", format="xml")
    """
    api_url = "https://nominatim.openstreetmap.org/lookup"
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }
    
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
    }.items() if v is not None}
    
    assert osm_ids is not None, 'Missing required parameter: osm_ids'
    
    response = requests.get(url=api_url, headers=headers,params=querystring, timeout=50)
    return response

if __name__ == '__main__':
    r = address_lookup(osm_ids="W50637691,N240109189", format="json", json_callback="myCallbackFunction", 
                      addressdetails=1, extratags=1, namedetails=1, accept_language="en-US,fr", 
                      polygon_geojson=1, polygon_threshold=0.01)
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