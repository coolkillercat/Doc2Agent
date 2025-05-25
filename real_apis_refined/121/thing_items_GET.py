import requests
from urllib.parse import quote
                
def thing_items(id=None, type=None, versions=None, videos=None, stats=None, historical=None, marketplace=None, comments=None, ratingcomments=None, page=1, pagesize=None, from=None, to=None):
    api_url = f"https://boardgamegeek.com/xmlapi2/thing?"
    querystring = {'id': id, 'type': type, 'versions': versions, 'videos': videos, 'stats': stats, 'historical': historical, 'marketplace': marketplace, 'comments': comments, 'ratingcomments': ratingcomments, 'page': page, 'pagesize': pagesize, 'from': from, 'to': to, }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = thing_items(id='''123,456''', type='''boardgame,boardgameexpansion''', versions=1, videos=1, stats=1, historical=1, marketplace=1, comments=1, ratingcomments=1, page=1, pagesize=50, from='''2023-01-01''', to='''2023-12-31''')
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

