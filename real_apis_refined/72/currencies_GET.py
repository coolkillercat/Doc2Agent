import requests
from urllib.parse import quote
                
def currencies(access_key=None, limit=100, offset=None):
    api_url = f"https://api.marketstack.com/v1/currencies"
    querystring = {'access_key': access_key, 'limit': limit}
    if offset is not None:
        querystring['offset'] = offset
    assert access_key is not None, 'Missing required parameter: access_key'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params={'access_key': access_key}, timeout=50, verify=False) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = currencies(access_key="YOUR_ACCESS_KEY", limit=50, offset=100)
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