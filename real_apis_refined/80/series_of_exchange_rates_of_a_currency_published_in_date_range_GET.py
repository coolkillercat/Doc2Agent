import requests
from urllib.parse import quote
                
def series_of_exchange_rates_of_a_currency_published_in_date_range(table=None, code=None, startDate=None, endDate=None):
    api_url = f"http://api.nbp.pl/api/exchangerates/rates/{quote(table, safe='')}/{quote(code, safe='')}/{quote(startDate, safe='')}/{quote(endDate, safe='')}/"
    querystring = {'table': table, 'code': code, 'startDate': startDate, 'endDate': endDate, }
    assert table is not None, 'Missing required parameter: table'
    assert code is not None, 'Missing required parameter: code'
    assert startDate is not None, 'Missing required parameter: startDate'
    assert endDate is not None, 'Missing required parameter: endDate'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = series_of_exchange_rates_of_a_currency_published_in_date_range(table='''A''', code='''USD''', startDate='''2022-01-01''', endDate='''2022-01-31''')
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

