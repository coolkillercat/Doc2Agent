import requests, json
from urllib.parse import quote


def tile_service(profile=None, x=None, y=None, zoom=None):
    api_url = f"http://router.project-osrm.org/tile/v1/{quote(profile, safe='')}/tile({quote(x, safe='')},{quote(y, safe='')},{quote(zoom, safe='')}).mvt"
    querystring = {'profile': profile, 'x': x, 'y': y, 'zoom': zoom, }
    assert profile is not None, 'Missing required parameter: profile'
    assert x is not None, 'Missing required parameter: x'
    assert y is not None, 'Missing required parameter: y'
    assert zoom is not None, 'Missing required parameter: zoom'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = tile_service(profile='''car''', x=1310, y=3166, zoom=13)
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

