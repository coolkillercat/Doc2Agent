import requests, json
from urllib.parse import quote


def reverse_geocoding(lat=None, lon=None, format='xml', json_callback='unset', addressdetails=1, extratags=None, namedetails=None, accept_language='browser language', zoom=18, layer='unset', polygon_geojson=None, polygon_threshold=None, email='unset', debug=None):
    api_url = f"https://nominatim.openstreetmap.org/reverse?lat={value}&lon={value}&{params}"
    querystring = {'lat': lat, 'lon': lon, 'format': format, 'json_callback': json_callback, 'addressdetails': addressdetails, 'extratags': extratags, 'namedetails': namedetails, 'accept_language': accept_language, 'zoom': zoom, 'layer': layer, 'polygon_geojson': polygon_geojson, 'polygon_threshold': polygon_threshold, 'email': email, 'debug': debug, }
    assert lat is not None, 'Missing required parameter: lat'
    assert lon is not None, 'Missing required parameter: lon'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = reverse_geocoding(lat=52.5487429714954, lon=-1.81602098644987, format='''json''', json_callback='''myCallbackFunction''', addressdetails=1, extratags=1, namedetails=1, accept_language='''en-US''', zoom=10, layer='''address,poi''', polygon_geojson=1, polygon_threshold=0.01, email='''user@example.com''', debug=1)
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

