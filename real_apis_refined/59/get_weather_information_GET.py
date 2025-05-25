import requests
from urllib.parse import quote
                
def get_weather_information(type=None, lang='is', stations=None, time='1h', anytime='0', types=None):
    api_url = f"https://apis.is/weather/{quote(type, safe='')}/{quote(lang, safe='')}"
    querystring = {'stations': stations, 'time': time, 'anytime': anytime, 'types': types}
    assert type is not None, 'Missing required parameter: type'
    assert lang is not None, 'Missing required parameter: lang'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50, verify=False) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_weather_information(type='''forecasts''', lang='''en''', stations='''1,422''', time='''1h''', anytime='''0''', types='''5,6''')
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