import requests
from urllib.parse import quote
                
def convert_json_to_jsonp(url=None, callback=None):
    api_url = f"https://json2jsonp.com/"
    querystring = {'url': url, 'callback': callback, }
    assert url is not None, 'Missing required parameter: url'
    assert callback is not None, 'Missing required parameter: callback'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = convert_json_to_jsonp(url='''http://domain.com/some/json''', callback='''cbfunc''')
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

