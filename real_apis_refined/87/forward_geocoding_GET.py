import requests
from urllib.parse import quote
                
def forward_geocoding(location=None, geoit='html', auth=None):
    api_url = f"https://geocode.xyz/location?geoit=outputformat&auth=your_api_key"
    querystring = {'location': location, 'geoit': geoit, 'auth': auth, }
    assert location is not None, 'Missing required parameter: location'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = forward_geocoding(location='''Hauptstr., 57632 Berzhausen''', geoit='''json''', auth='''your_api_key''')
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

