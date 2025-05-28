import requests, json
from urllib.parse import quote


def address_lookup(osm_ids=None, format='jsonv2', json_callback='unset', addressdetails=None, extratags=None, namedetails=None, accept_language='browser language', polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None, email='unset', debug=None):
    api_url = f"https://nominatim.openstreetmap.org/lookup?osm_ids=[N|W|R]{value},…,…,&{params}"
    querystring = {'osm_ids': osm_ids, 'format': format, 'json_callback': json_callback, 'addressdetails': addressdetails, 'extratags': extratags, 'namedetails': namedetails, 'accept_language': accept_language, 'polygon_geojson': polygon_geojson, 'polygon_kml': polygon_kml, 'polygon_svg': polygon_svg, 'polygon_text': polygon_text, 'polygon_threshold': polygon_threshold, 'email': email, 'debug': debug, }
    assert osm_ids is not None, 'Missing required parameter: osm_ids'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = address_lookup(osm_ids='''R146656,W104393803,N240109189''', format='''json''', json_callback='''myCallbackFunction''', addressdetails=1, extratags=1, namedetails=1, accept_language='''en-US''', polygon_geojson=1, polygon_kml=1, polygon_svg=1, polygon_text=1, polygon_threshold=0.01, email='''user@example.com''', debug=1)
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

