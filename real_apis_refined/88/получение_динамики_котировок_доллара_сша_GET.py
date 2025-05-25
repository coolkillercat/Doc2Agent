import requests
from urllib.parse import quote
                
def получение_динамики_котировок_доллара_сша(date_req1=None, date_req2=None, VAL_NM_RQ=None):
    api_url = f"http://www.cbr.ru/scripts/XML_dynamic.asp"
    querystring = {'date_req1': date_req1, 'date_req2': date_req2, 'VAL_NM_RQ': VAL_NM_RQ, }
    assert date_req1 is not None, 'Missing required parameter: date_req1'
    assert date_req2 is not None, 'Missing required parameter: date_req2'
    assert VAL_NM_RQ is not None, 'Missing required parameter: VAL_NM_RQ'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = получение_динамики_котировок_доллара_сша(date_req1='''02/03/2001''', date_req2='''14/03/2001''', VAL_NM_RQ='''R01235''')
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

