import requests
from urllib.parse import quote
                
def users(name=None, buddies=None, guilds=None, hot=None, top=None, domain='boardgame', page=1):
    api_url = f"https://boardgamegeek.com/xmlapi2/user?"
    querystring = {'name': name, 'buddies': buddies, 'guilds': guilds, 'hot': hot, 'top': top, 'domain': domain, 'page': page, }
    assert name is not None, 'Missing required parameter: name'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = users(name='''john_doe''', buddies=1, guilds=1, hot=1, top=1, domain='''rpg''', page=1)
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

