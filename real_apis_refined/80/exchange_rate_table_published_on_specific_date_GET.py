import requests
from urllib.parse import quote
                
def exchange_rate_table_published_on_specific_date(table=None, date=None):
    api_url = f"http://api.nbp.pl/api/exchangerates/tables/{quote(table, safe='')}/{quote(date, safe='')}/"
    querystring = {'table': table, 'date': date, }
    assert table is not None, 'Missing required parameter: table'
    assert date is not None, 'Missing required parameter: date'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = exchange_rate_table_published_on_specific_date(table='''A''', date='''2022-01-01''')
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

