import requests
from urllib.parse import quote
                
def draw_a_card(deck_id=None, count=1):
    api_url = f"https://deckofcardsapi.com/api/deck/{{quote(deck_id, safe='')}}/draw/?count=2"
    querystring = {'deck_id': deck_id, 'count': count, }
    assert deck_id is not None, 'Missing required parameter: deck_id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = draw_a_card(deck_id='''3p40paa87x90''', count=2)
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

