import requests
from urllib.parse import quote
                
def series_of_latest_exchange_rates_of_a_currency(table=None, code=None, topCount=None):
    api_url = f"http://api.nbp.pl/api/exchangerates/rates/{quote(str(table), safe='')}/{quote(str(code), safe='')}/last/{str(topCount)}/"
    querystring = {'table': table, 'code': code, 'topCount': topCount, }
    assert table is not None, 'Missing required parameter: table'
    assert code is not None, 'Missing required parameter: code'
    assert topCount is not None, 'Missing required parameter: topCount'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = series_of_latest_exchange_rates_of_a_currency(table='''A''', code='''USD''', topCount=10)
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