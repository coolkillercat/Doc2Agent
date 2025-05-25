import requests
from urllib.parse import quote
                
def query(action=None, format='json', list=None, meta=None, prop=None):
    api_url = f"https://en.wikipedia.org/w/api.php"
    querystring = {'action': action, 'format': format}
    
    # Only add non-None parameters to the querystring
    if list is not None:
        querystring['list'] = list
    if meta is not None:
        querystring['meta'] = meta
    if prop is not None:
        querystring['prop'] = prop
    
    assert action is not None, 'Missing required parameter: action'
    assert format is not None, 'Missing required parameter: format'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = query(action='query', format='json', list='allpages', meta='siteinfo', prop='info')
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