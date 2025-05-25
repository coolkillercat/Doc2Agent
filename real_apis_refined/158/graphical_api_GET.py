import requests
from urllib.parse import quote
                
def graphical_api(lon=None, lat=None, ac=None, lang='en', unit='metric', output='internal', tzshift=None):
    api_url = "http://www.7timer.info/bin/astro.php"
    
    # Handle the case where lat is a set of tuples
    if isinstance(lat, set):
        for item in lat:
            if isinstance(item, tuple) and len(item) == 2:
                lon = item[0]
                lat = item[1]
                break
    
    # Ensure required parameters are provided
    assert lon is not None, 'Missing required parameter: lon'
    assert lat is not None, 'Missing required parameter: lat'
    
    # Build query parameters
    querystring = {}
    querystring['lon'] = lon
    querystring['lat'] = lat
    if ac is not None:
        querystring['ac'] = ac
    if lang is not None:
        querystring['lang'] = lang
    if unit is not None:
        querystring['unit'] = unit
    if output is not None:
        querystring['output'] = output
    if tzshift is not None:
        querystring['tzshift'] = tzshift
    
    # Make the request
    response = requests.get(url=api_url, params=querystring, timeout=50)
    
    return response

if __name__ == '__main__':
    r = graphical_api(lon=113.17, lat=23.09, ac=0, lang='en', unit='metric', output='internal', tzshift=0)
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
    # Don't try to decode binary image data as UTF-8
    result_dict['content'] = r.content.decode('latin1')
    print(json.dumps(result_dict, indent=4))