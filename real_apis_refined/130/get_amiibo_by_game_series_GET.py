import requests
from urllib.parse import quote
                
def get_amiibo_by_game_series(gameseries=None):
    api_url = f"https://www.amiiboapi.com/api/amiibo/?gameseries={quote(gameseries, safe='')}"
    querystring = {'gameseries': gameseries, }
    assert gameseries is not None, 'Missing required parameter: gameseries'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_amiibo_by_game_series(gameseries='''zelda''')
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

