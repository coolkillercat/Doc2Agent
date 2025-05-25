import requests
from urllib.parse import quote
                
def plays(username=None, id=None, type=None, mindate=None, maxdate=None, subtype='boardgame', page=1):
    api_url = f"https://boardgamegeek.com/xmlapi2/plays?"
    querystring = {'username': username, 'id': id, 'type': type, 'mindate': mindate, 'maxdate': maxdate, 'subtype': subtype, 'page': page, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = plays(username='''john_doe''', id='''123''', type='''thing''', mindate='''2023-01-01''', maxdate='''2023-12-31''', subtype='''boardgame''', page=1)
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

