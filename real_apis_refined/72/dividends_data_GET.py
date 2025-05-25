import requests
from urllib.parse import quote
                
def dividends_data(access_key=None, symbols=None, sort='DESC', date_from=None, date_to=None, limit=100, offset=None):
    api_url = f"https://api.marketstack.com/v1/dividends"
    querystring = {'access_key': access_key, 'symbols': symbols, 'sort': sort, 'date_from': date_from, 'date_to': date_to, 'limit': limit, 'offset': offset}
    assert access_key is not None, 'Missing required parameter: access_key'
    assert symbols is not None, 'Missing required parameter: symbols'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params={'access_key': access_key, 'symbols': symbols}, timeout=50, verify=False)
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = dividends_data(access_key="YOUR_ACCESS_KEY", symbols="AAPL,MSFT", sort="ASC", date_from="2020-05-21", date_to="2020-05-23", limit=50, offset=100)
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