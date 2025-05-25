import requests
from urllib.parse import quote
                
def reshuffle_the_cards(deck_id=None, remaining=None):
    api_url = f"https://deckofcardsapi.com/api/deck/{{quote(deck_id, safe='')}}/shuffle/?remaining=true"
    querystring = {'deck_id': deck_id, 'remaining': remaining, }
    assert deck_id is not None, 'Missing required parameter: deck_id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = reshuffle_the_cards(deck_id='''3p40paa87x90''', remaining=True)
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

