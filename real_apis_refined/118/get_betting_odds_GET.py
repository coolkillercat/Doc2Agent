import requests
from urllib.parse import quote
                
def get_betting_odds(date=None, game_id=None):
    api_url = f"https://api.balldontlie.io/v1/odds"
    querystring = {'date': date, 'game_id': game_id, }
    assert date is not None, 'Missing required parameter: date'
    assert game_id is not None, 'Missing required parameter: game_id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_betting_odds(date='''2024-04-01''', game_id=1)
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

