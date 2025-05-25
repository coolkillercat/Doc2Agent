import requests
from urllib.parse import quote
                
def reverse_geocoding(latitude_longitude=None, geoit='html', auth=None):
    api_url = f"https://geocode.xyz/latitude,longitude?geoit=outputformat&auth=your_api_key"
    querystring = {'latitude_longitude': latitude_longitude, 'geoit': geoit, 'auth': auth, }
    assert latitude_longitude is not None, 'Missing required parameter: latitude_longitude'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = reverse_geocoding(latitude_longitude='''51.50354,-0.12768''', geoit='''json''', auth='''your_api_key''')
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

