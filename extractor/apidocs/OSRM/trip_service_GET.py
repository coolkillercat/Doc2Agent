import requests, json
from urllib.parse import quote


def trip_service(profile=None, coordinates=None, steps=None, geometries='polyline', overview='simplified', annotations=None):
    api_url = f"http://router.project-osrm.org/trip/v1/{quote(profile, safe='')}/{quote(coordinates, safe='')}?steps={true|false}&geometries={polyline|polyline6|geojson}&overview={simplified|full|false}&annotations={true|false}"
    querystring = {'profile': profile, 'coordinates': coordinates, 'steps': steps, 'geometries': geometries, 'overview': overview, 'annotations': annotations, }
    assert profile is not None, 'Missing required parameter: profile'
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = trip_service(profile='''driving''', coordinates='''13.388860,52.517037;13.397634,52.529407;13.428555,52.523219''', steps=True, geometries='''geojson''', overview='''full''', annotations=True)
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

