import requests
from urllib.parse import quote
                
def guilds(id=None, members=None, sort='username', page=1):
    api_url = f"https://boardgamegeek.com/xmlapi2/guild?"
    querystring = {'id': id, 'members': members, 'sort': sort, 'page': page, }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = guilds(id='''123''', members=1, sort='''date''', page=1)
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

