import requests, json
from urllib.parse import quote


def search(q=None, amenity=None, street=None, city=None, county=None, state=None, country=None, postalcode=None, format='jsonv2', json_callback=None, limit=10, addressdetails=None, extratags=None, namedetails=None, accept_language=None, countrycodes=None, layer=None, featureType=None, exclude_place_ids=None, viewbox=None, bounded=None, polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None, email=None, dedupe=1, debug=None):
    """
    Search for locations using the Nominatim OpenStreetMap API.
    
    Parameters:
    -----------
    q : str, optional
        Free-form query string to search for.
        Example: 'birmingham, pilkington avenue'
    amenity : str, optional
        Name and/or type of POI.
        Example: 'pub'
    street : str, optional
        Housenumber and streetname.
        Example: '135 Pilkington Avenue'
    city : str, optional
        City name.
        Example: 'Birmingham'
    county : str, optional
        County name.
        Example: 'West Midlands'
    state : str, optional
        State name.
        Example: 'England'
    country : str, optional
        Country name.
        Example: 'United Kingdom'
    postalcode : str, optional
        Postal code.
        Example: 'B72 1LH'
    format : str, optional
        Output format. One of: 'xml', 'json', 'jsonv2', 'geojson', 'geocodejson'.
        Default: 'jsonv2'
    json_callback : str, optional
        Function name for JSONP callback.
        Example: 'myCallback'
    limit : int, optional
        Maximum number of returned results. Cannot be more than 40.
        Default: 10
    addressdetails : int, optional
        Include a breakdown of the address into elements (0 or 1).
        Default: 0
    extratags : int, optional
        Include additional information in the result (0 or 1).
        Default: 0
    namedetails : int, optional
        Include a list of alternative names in the results (0 or 1).
        Default: 0
    accept_language : str, optional
        Preferred language order for showing search results.
        Example: 'en-US'
    countrycodes : str, optional
        Limit search to certain countries.
        Example: 'gb,de'
    layer : str, optional
        Filter by theme. Comma-separated list of: 'address', 'poi', 'railway', 'natural', 'manmade'.
        Example: 'address,poi'
    featureType : str, optional
        Filter by feature type. One of: 'country', 'state', 'city', 'settlement'.
        Example: 'city'
    exclude_place_ids : str, optional
        Comma-separated list of place IDs to exclude from results.
        Example: '125279639'
    viewbox : str, optional
        Boost results in this bounding box. Format: '<x1>,<y1>,<x2>,<y2>'.
        Example: '13.0884,52.3383,13.7611,52.6755'
    bounded : int, optional
        Turn viewbox into a filter (0 or 1).
        Default: 0
    polygon_geojson : int, optional
        Add GeoJSON geometry to the result (0 or 1).
        Default: 0
    polygon_kml : int, optional
        Add KML geometry to the result (0 or 1).
        Default: 0
    polygon_svg : int, optional
        Add SVG geometry to the result (0 or 1).
        Default: 0
    polygon_text : int, optional
        Add WKT geometry to the result (0 or 1).
        Default: 0
    polygon_threshold : float, optional
        Simplify geometry with this tolerance.
        Example: 0.01
    email : str, optional
        Email address for large numbers of requests.
        Example: 'user@example.com'
    dedupe : int, optional
        Enable or disable deduplication (0 or 1).
        Default: 1
    debug : int, optional
        Output debug information (0 or 1).
        Default: 0
    
    Returns:
    --------
    requests.Response
        The response from the API.
        
    Examples:
    ---------
    # Free-form query
    search(q='birmingham, pilkington avenue')
    
    # Structured query
    search(street='135 Pilkington Avenue', city='Birmingham', country='United Kingdom')
    """
    api_url = "https://nominatim.openstreetmap.org/search"
    querystring = {}
    
    # Either use free-form query or structured query, not both
    if q is not None:
        querystring['q'] = q
    else:
        # Add structured query parameters only if q is not provided
        if amenity is not None:
            querystring['amenity'] = amenity
        if street is not None:
            querystring['street'] = street
        if city is not None:
            querystring['city'] = city
        if county is not None:
            querystring['county'] = county
        if state is not None:
            querystring['state'] = state
        if country is not None:
            querystring['country'] = country
        if postalcode is not None:
            querystring['postalcode'] = postalcode
    
    # Add other parameters
    if format is not None:
        querystring['format'] = format
    if json_callback is not None:
        querystring['json_callback'] = json_callback
    if limit is not None:
        querystring['limit'] = limit
    if addressdetails is not None:
        querystring['addressdetails'] = addressdetails
    if extratags is not None:
        querystring['extratags'] = extratags
    if namedetails is not None:
        querystring['namedetails'] = namedetails
    if accept_language is not None:
        querystring['accept-language'] = accept_language
    if countrycodes is not None:
        querystring['countrycodes'] = countrycodes
    if layer is not None:
        querystring['layer'] = layer
    if featureType is not None:
        querystring['featureType'] = featureType
    if exclude_place_ids is not None:
        querystring['exclude_place_ids'] = exclude_place_ids
    if viewbox is not None:
        querystring['viewbox'] = viewbox
    if bounded is not None:
        querystring['bounded'] = bounded
    if polygon_geojson is not None:
        querystring['polygon_geojson'] = polygon_geojson
    if polygon_kml is not None:
        querystring['polygon_kml'] = polygon_kml
    if polygon_svg is not None:
        querystring['polygon_svg'] = polygon_svg
    if polygon_text is not None:
        querystring['polygon_text'] = polygon_text
    if polygon_threshold is not None:
        querystring['polygon_threshold'] = polygon_threshold
    if email is not None:
        querystring['email'] = email
    if dedupe is not None:
        querystring['dedupe'] = dedupe
    if debug is not None:
        querystring['debug'] = debug
    
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    # Example using free-form query
    r = search(q='birmingham, pilkington avenue', format='json', limit=5, addressdetails=1)
    
    # Example using structured query
    # r = search(street='135 Pilkington Avenue', city='Birmingham', country='United Kingdom', format='json', limit=5, addressdetails=1)
    
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