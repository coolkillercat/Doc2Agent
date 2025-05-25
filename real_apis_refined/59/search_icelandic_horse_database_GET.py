import requests
from urllib.parse import quote
                
def search_icelandic_horse_database(id=None, name=None, origin=None, microchip=None):
    api_url = f"https://apis.is/horses"
    querystring = {'id': id, 'name': name, 'origin': origin, 'microchip': microchip}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50, verify=False) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = search_icelandic_horse_database(id='''IS1987187700''', name='''Oddur frá Selfossi''', origin='''Selfoss''', microchip='''1234567890''')
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