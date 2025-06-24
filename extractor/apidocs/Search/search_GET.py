import requests, json
from urllib.parse import quote


def search(q=None, amenity=None, street=None, city=None, county=None, state=None, country=None, postalcode=None, format='jsonv2', json_callback=None, limit=10, addressdetails=None, extratags=None, namedetails=None, accept_language='browser language', countrycodes=None, layer=None, featureType=None, exclude_place_ids=None, viewbox=None, bounded=None, polygon_geojson=None, polygon_kml=None, polygon_svg=None, polygon_text=None, polygon_threshold=None, email=None, dedupe=1, debug=None):
    api_url = f"https://nominatim.openstreetmap.org/search?{params}"
    querystring = {'q': q, 'amenity': amenity, 'street': street, 'city': city, 'county': county, 'state': state, 'country': country, 'postalcode': postalcode, 'format': format, 'json_callback': json_callback, 'limit': limit, 'addressdetails': addressdetails, 'extratags': extratags, 'namedetails': namedetails, 'accept_language': accept_language, 'countrycodes': countrycodes, 'layer': layer, 'featureType': featureType, 'exclude_place_ids': exclude_place_ids, 'viewbox': viewbox, 'bounded': bounded, 'polygon_geojson': polygon_geojson, 'polygon_kml': polygon_kml, 'polygon_svg': polygon_svg, 'polygon_text': polygon_text, 'polygon_threshold': polygon_threshold, 'email': email, 'dedupe': dedupe, 'debug': debug, }
    headers = {
        'User-Agent': 'Nominatim-API-Client/1.0',
    }
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = search(q='''birmingham, pilkington avenue''', amenity='''pub''', street='''135 Pilkington Avenue''', city='''Birmingham''', county='''West Midlands''', state='''England''', country='''United Kingdom''', postalcode='''B72 1LH''', format='''json''', json_callback='''myCallback''', limit=5, addressdetails=1, extratags=1, namedetails=1, accept_language='''en-US''', countrycodes='''gb,de''', layer='''address,poi''', featureType='''city''', exclude_place_ids='''125279639''', viewbox='''13.0884,52.3383,13.7611,52.6755''', bounded=1, polygon_geojson=1, polygon_kml=1, polygon_svg=1, polygon_text=1, polygon_threshold=0.01, email='''user@example.com''', dedupe=0, debug=1)
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

