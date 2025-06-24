import requests, json
from urllib.parse import quote


def place_details(osmtype=None, osmid=None, class=None, json_callback='unset', addressdetails=None, keywords=None, linkedplaces=1, hierarchy=None, group_hierarchy=None, polygon_geojson=None, accept_language='content of 'Accept-Language' HTTP header'):
    api_url = f"https://nominatim.openstreetmap.org/details?osmtype=[N|W|R]&osmid={value}&class={value}"
    querystring = {'osmtype': osmtype, 'osmid': osmid, 'class': class, 'json_callback': json_callback, 'addressdetails': addressdetails, 'keywords': keywords, 'linkedplaces': linkedplaces, 'hierarchy': hierarchy, 'group_hierarchy': group_hierarchy, 'polygon_geojson': polygon_geojson, 'accept_language': accept_language, }
    assert osmtype is not None, 'Missing required parameter: osmtype'
    assert osmid is not None, 'Missing required parameter: osmid'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = place_details(osmtype='''W''', osmid=38210407, class='''tourism''', json_callback='''myCallbackFunction''', addressdetails=1, keywords=1, linkedplaces=1, hierarchy=1, group_hierarchy=1, polygon_geojson=1, accept_language='''en-US,fr''')
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

