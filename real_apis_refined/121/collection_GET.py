import requests
from urllib.parse import quote
                
def collection(username=None, version=None, subtype='boardgame', excludesubtype=None, id=None, brief=None, stats=None, own=None, rated=None, played=None, comment=None, trade=None, want=None, wishlist=None, wishlistpriority=None, preordered=None, wanttoplay=None, wanttobuy=None):
    api_url = f"https://boardgamegeek.com/xmlapi2/collection?"
    querystring = {'username': username, 'version': version, 'subtype': subtype, 'excludesubtype': excludesubtype, 'id': id, 'brief': brief, 'stats': stats, 'own': own, 'rated': rated, 'played': played, 'comment': comment, 'trade': trade, 'want': want, 'wishlist': wishlist, 'wishlistpriority': wishlistpriority, 'preordered': preordered, 'wanttoplay': wanttoplay, 'wanttobuy': wanttobuy, }
    assert username is not None, 'Missing required parameter: username'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = collection(username='''john_doe''', version=1, subtype='''boardgame''', excludesubtype='''boardgameexpansion''', id='''123,456''', brief=1, stats=1, own=1, rated=1, played=1, comment=1, trade=1, want=1, wishlist=1, wishlistpriority=1, preordered=1, wanttoplay=1, wanttobuy=1)
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

