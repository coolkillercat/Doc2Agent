import requests, json
from urllib.parse import quote


def place_details(osmtype=None, osmid=None, class_param=None, place_id=None, json_callback='_unset_', pretty=None, addressdetails=None, keywords=None, linkedplaces=1, hierarchy=None, group_hierarchy=None, polygon_geojson=None, accept_language=None):
    """
    Show all details about a single place saved in the database.
    
    This API endpoint is meant for visual inspection of the data in the database.
    The parameters of the endpoint and the output may change occasionally between
    versions of Nominatim.
    
    Parameters:
    -----------
    osmtype : str
        One of node (N), way (W) or relation (R).
    osmid : int
        The OSM ID must be a number.
    class_param : str
        Optional parameter to distinguish between entries when the corresponding OSM object has more than one main tag.
    place_id : int
        Place ID assigned sequentially during Nominatim data import.
    json_callback : str, default='_unset_'
        When set, JSON output will be wrapped in a callback function with the given name.
    pretty : int, default=None
        Add indentation to the output to make it more human-readable (0 or 1).
    addressdetails : int, default=None
        When set to 1, include a breakdown of the address into elements.
    keywords : int, default=None
        When set to 1, include a list of name keywords and address keywords in the result.
    linkedplaces : int, default=1
        Include details of places that are linked with this one.
    hierarchy : int, default=None
        Include details of places lower in the address hierarchy.
    group_hierarchy : int, default=None
        When set to 1, the output of the address hierarchy will be grouped by type.
    polygon_geojson : int, default=None
        Include geometry of result.
    accept_language : str, default=None
        Preferred language order for showing search results.
    
    Examples:
    ---------
    >>> place_details(osmtype='W', osmid=38210407, class_param='tourism')
    >>> place_details(place_id=85993608, pretty=1, addressdetails=1)
    """
    api_url = "https://nominatim.openstreetmap.org/details"
    querystring = {
        'osmtype': osmtype, 
        'osmid': osmid, 
        'class': class_param, 
        'place_id': place_id, 
        'json_callback': json_callback if json_callback != '_unset_' else None, 
        'pretty': pretty, 
        'addressdetails': addressdetails, 
        'keywords': keywords, 
        'linkedplaces': linkedplaces, 
        'hierarchy': hierarchy, 
        'group_hierarchy': group_hierarchy, 
        'polygon_geojson': polygon_geojson, 
        'accept-language': accept_language
    }
    
    # Remove None values from querystring
    querystring = {k: v for k, v in querystring.items() if v is not None}
    
    # Check required parameters based on the API endpoint being used
    if place_id is None:
        assert osmtype is not None, 'Missing required parameter: osmtype'
        assert osmid is not None, 'Missing required parameter: osmid'
    
    response = requests.get(url=api_url, params=querystring, timeout=50)
    return response

if __name__ == '__main__':
    r = place_details(osmtype='W', osmid=38210407, class_param='tourism', place_id=85993608, json_callback='myCallback', pretty=1, addressdetails=1, keywords=1, linkedplaces=1, hierarchy=1, group_hierarchy=1, polygon_geojson=1, accept_language='en-US,fr')
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