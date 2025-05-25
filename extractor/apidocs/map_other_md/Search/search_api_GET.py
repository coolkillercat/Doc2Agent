import requests, json
from urllib.parse import quote


def search_api(q=None, amenity=None, street=None, city=None, county=None, state=None, country=None, postalcode=None, format='jsonv2', json_callback='_unset_', limit=10, addressdetails=None, extratags=None, namedetails=None, accept_language=None, countrycodes='_unset_', layer='_unset_', featureType='_unset_', exclude_place_ids=None, viewbox='_unset_', bounded=None, polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None):
    """
    Search for places using the Nominatim OpenStreetMap API.
    
    Parameters:
    -----------
    q : str, optional
        Free-form query string
    amenity : str, optional
        Amenity type to search for
    street : str, optional
        Street name
    city : str, optional
        City name
    county : str, optional
        County name
    state : str, optional
        State name
    country : str, optional
        Country name
    postalcode : str, optional
        Postal code
    format : str, default 'jsonv2'
        Output format (json, jsonv2, xml, etc.)
    json_callback : str, default '_unset_'
        Callback function name for JSONP requests
    limit : int, default 10
        Maximum number of results to return
    addressdetails : int, optional
        Include address details in results (0 or 1)
    extratags : int, optional
        Include additional tags in results (0 or 1)
    namedetails : int, optional
        Include name details in results (0 or 1)
    accept_language : str, optional
        Preferred language for results
    countrycodes : str, default '_unset_'
        Limit search to specified countries (comma-separated)
    layer : str, default '_unset_'
        Limit search to specified layers (comma-separated)
    featureType : str, default '_unset_'
        Limit search to specified feature types
    exclude_place_ids : str, optional
        Exclude places with specified IDs (comma-separated)
    viewbox : str, default '_unset_'
        Search within specified bounding box
    bounded : int, optional
        Restrict search to viewbox (0 or 1)
    polygon_geojson : int, optional
        Return geometry as GeoJSON (0 or 1)
    polygon_kml : int, optional
        Return geometry as KML (0 or 1)
    polygon_svg : int, optional
        Return geometry as SVG (0 or 1)
    polygon_text : int, optional
        Return geometry as WKT (0 or 1)
    polygon_threshold : float, optional
        Simplification threshold for polygon geometries
    
    Returns:
    --------
    requests.Response
        API response object
    
    Examples:
    ---------
    >>> response = search_api(q="Birmingham", format="json", limit=5)
    >>> response = search_api(street="135 Pilkington Avenue", city="Birmingham", country="UK", format="json")
    >>> response = search_api(q="restaurants in London", amenity="restaurant", country="UK", limit=10)
    """
    api_url = "https://nominatim.openstreetmap.org/search"
    querystring = {
        'q': q, 
        'amenity': amenity, 
        'street': street, 
        'city': city, 
        'county': county, 
        'state': state, 
        'country': country, 
        'postalcode': postalcode, 
        'format': format, 
        'json_callback': json_callback if json_callback != '_unset_' else None, 
        'limit': limit, 
        'addressdetails': addressdetails, 
        'extratags': extratags, 
        'namedetails': namedetails, 
        'accept-language': accept_language, 
        'countrycodes': countrycodes if countrycodes != '_unset_' else None, 
        'layer': layer if layer != '_unset_' else None, 
        'featureType': featureType if featureType != '_unset_' else None, 
        'exclude_place_ids': exclude_place_ids, 
        'viewbox': viewbox if viewbox != '_unset_' else None, 
        'bounded': bounded, 
        'polygon_geojson': polygon_geojson, 
        'polygon_kml': polygon_kml, 
        'polygon_svg': polygon_svg, 
        'polygon_text': polygon_text, 
        'polygon_threshold': polygon_threshold
    }
    
    # Remove None values
    querystring = {k: v for k, v in querystring.items() if v is not None}
    
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }

    
    try:
        response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
        if response.status_code != 200:
            # Try again without parameters that might be causing issues
            simplified_params = {'q': q, 'format': format}
            response = requests.get(url=api_url, params=simplified_params, headers=headers, timeout=50)
        return response
    except Exception as e:
        print(f"Error making request: {e}")
        return None

if __name__ == '__main__':
    r = search_api(q='birmingham, pilkington avenue', amenity='restaurant', street='135 Pilkington Avenue', city='Birmingham', county='West Midlands', state='England', country='United Kingdom', postalcode='B72 1LH', format='json', json_callback='myCallback', limit=5, addressdetails=1, extratags=1, namedetails=1, accept_language='en-US,fr', countrycodes='gb,de', layer='poi,natural', featureType='city', exclude_place_ids='12345,67890', viewbox='13.397,52.517,13.398,52.518', bounded=1, polygon_geojson=1, polygon_kml=1, polygon_svg=1, polygon_text=1, polygon_threshold=0.01)
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