import requests
from urllib.parse import quote
                
def day_summary(coin=None, year=None, month=None, day=None):
    api_url = f"https://www.mercadobitcoin.net/api/{quote(str(coin), safe='')}/day-summary/{str(year)}/{str(month)}/{str(day)}/"
    querystring = {'coin': coin, 'year': year, 'month': month, 'day': day, }
    assert coin is not None, 'Missing required parameter: coin'
    assert year is not None, 'Missing required parameter: year'
    assert month is not None, 'Missing required parameter: month'
    assert day is not None, 'Missing required parameter: day'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = day_summary(coin='''BTC''', year=2013, month=6, day=20)
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