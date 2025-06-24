import requests, json
from urllib.parse import quote


def place_details(osmtype=None, osmid=None, osm_class=None, place_id=None, json_callback=None, addressdetails=None, keywords=None, linkedplaces=1, hierarchy=None, group_hierarchy=None, polygon_geojson=None, accept_language=None, format='json'):
    """
    Show all details about a single place saved in the database.
    
    Parameters:
    -----------
    osmtype : str
        One of node (N), way (W) or relation (R).
    osmid : int
        The OSM ID must be a number.
    osm_class : str
        Allows to distinguish between entries when the corresponding OSM object has more than one main tag.
    place_id : int
        Place ID assigned sequentially during Nominatim data import.
    json_callback : str
        When set, JSON output will be wrapped in a callback function with the given name.
    addressdetails : int
        When set to 1, include a breakdown of the address into elements.
    keywords : int
        When set to 1, include a list of name keywords and address keywords in the result.
    linkedplaces : int
        Include details of places that are linked with this one.
    hierarchy : int
        Include details of POIs and address that depend on the place.
    group_hierarchy : int
        When set to 1, the output of the address hierarchy will be grouped by type.
    polygon_geojson : int
        Include geometry of result.
    accept_language : str
        Preferred language order for showing search results.
    format : str
        Output format (json is recommended).
        
    Examples:
    ---------
    >>> place_details(osmtype='W', osmid=38210407)
    >>> place_details(place_id=85993608, addressdetails=1, keywords=1)
    """
    api_url = "https://nominatim.openstreetmap.org/details"
    querystring = {
        'osmtype': osmtype, 
        'osmid': osmid, 
        'class': osm_class, 
        'place_id': place_id, 
        'json_callback': json_callback, 
        'addressdetails': addressdetails, 
        'keywords': keywords, 
        'linkedplaces': linkedplaces, 
        'hierarchy': hierarchy, 
        'group_hierarchy': group_hierarchy, 
        'polygon_geojson': polygon_geojson,
        'format': format
    }
    
    if accept_language:
        querystring['accept-language'] = accept_language
    
    # Remove None values
    querystring = {k: v for k, v in querystring.items() if v is not None}
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }
    # Check required parameters based on request format
    if place_id is None:
        if osmtype is None or osmid is None:
            raise ValueError('Either place_id or both osmtype and osmid must be provided')
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = place_details(osmtype='W', osmid=38210407)
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