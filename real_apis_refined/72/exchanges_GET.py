import requests
from urllib.parse import quote
                
def exchanges(access_key=None, search=None, limit=100, offset=None):
    api_url = f"https://api.marketstack.com/v1/exchanges"
    querystring = {'access_key': access_key, 'search': search, 'limit': limit, 'offset': offset}
    assert access_key is not None, 'Missing required parameter: access_key'
    
    # Remove None values from querystring
    querystring = {k: v for k, v in querystring.items() if v is not None}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params={'access_key': access_key}, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = exchanges(access_key="YOUR_ACCESS_KEY", search="XNAS", limit=50, offset=100)
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