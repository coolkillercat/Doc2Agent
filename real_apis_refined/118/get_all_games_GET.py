import requests
from urllib.parse import quote
                
def get_all_games(cursor=None, per_page=None, dates=None, seasons=None, team_ids=None, postseason=None, start_date=None, end_date=None):
    api_url = f"https://api.balldontlie.io/v1/games"
    querystring = {'cursor': cursor, 'per_page': per_page, 'dates': dates, 'seasons': seasons, 'team_ids': team_ids, 'postseason': postseason, 'start_date': start_date, 'end_date': end_date}
    
    headers = {
        'Authorization': 'Bearer YOUR_ACTUAL_API_KEY'  # Replace YOUR_API_KEY_HERE with your actual API key
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_all_games(cursor=25, per_page=25, dates=['2024-01-01', '2024-01-02'], seasons=['2022', '2023'], team_ids=[1, 2], postseason=False, start_date='2024-01-01', end_date='2024-01-31')
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