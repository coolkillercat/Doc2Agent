import requests
from urllib.parse import quote
                
def adding_to_piles(deck_id=None, pile_name=None, cards=None):
    api_url = f"https://deckofcardsapi.com/api/deck/{{quote(deck_id, safe='')}}/pile/{{quote(pile_name, safe='')}}/add/?cards=AS,2S"
    querystring = {'deck_id': deck_id, 'pile_name': pile_name, 'cards': cards, }
    assert deck_id is not None, 'Missing required parameter: deck_id'
    assert pile_name is not None, 'Missing required parameter: pile_name'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = adding_to_piles(deck_id='''3p40paa87x90''', pile_name='''discard''', cards='''AS,2S''')
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

