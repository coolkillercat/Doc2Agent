import requests, json
from urllib.parse import quote


def search_api(q=None, amenity=None, street=None, city=None, county=None, state=None, country=None, postalcode=None, format='jsonv2', json_callback=None, limit=10, addressdetails=None, extratags=None, namedetails=None, accept_language=None, countrycodes=None, layer=None, featureType=None, exclude_place_ids=None, viewbox=None, bounded=None, polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None):
    """
    Search for locations using the search API.
    
    Parameters:
    -----------
    q : str, optional
        Free-form query string to search for.
    amenity : str, optional
        Name and/or type of POI.
    street : str, optional
        Housenumber and streetname.
    city : str, optional
        City name.
    county : str, optional
        County name.
    state : str, optional
        State name.
    country : str, optional
        Country name.
    postalcode : str, optional
        Postal code.
    format : str, optional
        Output format. One of: 'xml', 'json', 'jsonv2', 'geojson', 'geocodejson'. Default is 'jsonv2'.
    json_callback : str, optional
        Function name for JSONP callback.
    limit : int, optional
        Maximum number of returned results. Default is 10.
    addressdetails : int, optional
        Include a breakdown of the address into elements (0 or 1).
    extratags : int, optional
        Include additional information in the result (0 or 1).
    namedetails : int, optional
        Include a full list of names for the result (0 or 1).
    accept_language : str, optional
        Preferred language order for showing search results.
    countrycodes : str, optional
        Comma-separated list of country codes to filter results.
    layer : str, optional
        Comma-separated list of layers to filter results.
    featureType : str, optional
        Type of feature to filter results.
    exclude_place_ids : str, optional
        Comma-separated list of place IDs to exclude from results.
    viewbox : str, optional
        Bounding box to focus search on, format: '<x1>,<y1>,<x2>,<y2>'.
    bounded : int, optional
        When set to 1, restricts results to the viewbox (0 or 1).
    polygon_geojson : int, optional
        Include GeoJSON polygon geometry in results (0 or 1).
    polygon_kml : int, optional
        Include KML polygon geometry in results (0 or 1).
    polygon_svg : int, optional
        Include SVG polygon geometry in results (0 or 1).
    polygon_text : int, optional
        Include WKT polygon geometry in results (0 or 1).
    polygon_threshold : float, optional
        Simplification threshold for polygon geometry.
    
    Returns:
    --------
    requests.Response
        The API response object.
    
    Examples:
    ---------
    >>> search_api(q="Birmingham, pilkington avenue")
    >>> search_api(street="135 Pilkington Avenue", city="Birmingham", country="United Kingdom", format="json")
    >>> search_api(q="bakery in berlin", limit=5, addressdetails=1)
    """
    api_url = "https://nominatim.openstreetmap.org/search?"
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }
    
    # Build query parameters, excluding None values
    querystring = {}
    if q is not None:
        querystring['q'] = q
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
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50)
    return response

if __name__ == '__main__':
    r = search_api(q='birmingham, pilkington avenue', format='json', limit=5, addressdetails=1)
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