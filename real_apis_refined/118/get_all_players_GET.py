import requests
from urllib.parse import quote
                
def get_all_players(cursor=None, per_page=None, search=None, first_name=None, last_name=None, team_ids=None, player_ids=None):
    api_url = f"https://api.balldontlie.io/v1/players"
    querystring = {}
    if cursor is not None:
        querystring['cursor'] = cursor
    if per_page is not None:
        querystring['per_page'] = per_page
    if search is not None:
        querystring['search'] = search
    if first_name is not None:
        querystring['first_name'] = first_name
    if last_name is not None:
        querystring['last_name'] = last_name
    if team_ids is not None:
        querystring['team_ids[]'] = team_ids
    if player_ids is not None:
        querystring['player_ids[]'] = player_ids
    
    headers = {
        "Authorization": "YOUR_API_KEY_HERE"  # Replace with actual API key
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_all_players(cursor=25, per_page=25, search='davis', first_name='anthony', last_name='davis', team_ids=[1, 2], player_ids=[1, 2])
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