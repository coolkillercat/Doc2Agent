import requests, json
from urllib.parse import quote


def table_service(profile=None, coordinates=None, sources='all', destinations='all'):
    api_url = f"http://router.project-osrm.org/table/v1/{quote(profile, safe='')}/{quote(coordinates, safe='')}?sources={index};{index}[;{index}_...]&destinations={index};{index}[;{index}_...]"
    querystring = {'profile': profile, 'coordinates': coordinates, 'sources': sources, 'destinations': destinations, }
    assert profile is not None, 'Missing required parameter: profile'
    assert coordinates is not None, 'Missing required parameter: coordinates'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = table_service(profile='''driving''', coordinates='''13.388860,52.517037;13.397634,52.529407;13.428555,52.523219''', sources='''0;5;7''', destinations='''5;1;4;2;3;6''')
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

