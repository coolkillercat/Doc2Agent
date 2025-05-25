import requests
from urllib.parse import quote
                
def get_all_advanced_stats(cursor=None, per_page=None, player_ids=None, game_ids=None, dates=None, seasons=None, postseason=None, start_date=None, end_date=None):
    api_url = f"https://api.balldontlie.io/v1/stats/advanced"
    querystring = {}
    
    if cursor is not None:
        querystring['cursor'] = cursor
    if per_page is not None:
        querystring['per_page'] = per_page
    if player_ids is not None:
        querystring['player_ids[]'] = player_ids
    if game_ids is not None:
        querystring['game_ids[]'] = game_ids
    if dates is not None:
        querystring['dates[]'] = dates
    if seasons is not None:
        querystring['seasons[]'] = seasons
    if postseason is not None:
        querystring['postseason'] = postseason
    if start_date is not None:
        querystring['start_date'] = start_date
    if end_date is not None:
        querystring['end_date'] = end_date
    
    headers = {
        "Authorization": "Bearer YOUR_ACTUAL_API_KEY"  # Replace with actual API key
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_all_advanced_stats(cursor=25, per_page=25, player_ids=[1, 2], game_ids=[1, 2], dates=['2024-01-01', '2024-01-02'], seasons=['2022', '2023'], postseason=False, start_date='2024-01-01', end_date='2024-01-31')
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