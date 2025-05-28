import requests, json
from urllib.parse import quote


def nearest_service(profile=None, coordinates=None, number=1, bearings=None):
    api_url = f"http://router.project-osrm.org/nearest/v1/{quote(profile, safe='')}/{quote(coordinates, safe='')}.json?number={number}"
    querystring = {'profile': profile, 'coordinates': coordinates, 'number': number, 'bearings': bearings, }
    assert profile is not None, 'Missing required parameter: profile'
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = nearest_service(profile='''driving''', coordinates='''13.388860,52.517037''', number=3, bearings='''0,20''')
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

