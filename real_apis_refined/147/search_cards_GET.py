import requests
from urllib.parse import quote
                
def search_cards(q=None, unique='cards', order='name', dir='auto', include_extras=None, include_multilingual=None, include_variations=None, page=1):
    api_url = f"https://api.scryfall.com/cards/search"
    querystring = {'q': q, 'unique': unique, 'order': order, 'dir': dir, 'include_extras': include_extras, 'include_multilingual': include_multilingual, 'include_variations': include_variations, 'page': page, }
    assert q is not None, 'Missing required parameter: q'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = search_cards(q='''goblin''', unique='''art''', order='''set''', dir='''desc''', include_extras=True, include_multilingual=True, include_variations=True, page=2)
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

