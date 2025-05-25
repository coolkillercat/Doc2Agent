import requests
from urllib.parse import quote
                
def get_top_50_stocks_discussed_on_reddit_wallstreetbets(date=None):
    api_url = f"https://tradestie.com/api/v1/apps/reddit"
    querystring = {'date': date, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_top_50_stocks_discussed_on_reddit_wallstreetbets(date='''2022-04-03''')
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

