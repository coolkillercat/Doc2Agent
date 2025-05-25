import requests
from urllib.parse import quote
                
def http_headers_capture(access_key=None, url=None, viewport='375x667', user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4', accept_lang='es-ES'):
    api_url = f"https://api.screenshotlayer.com/api/capture"
    assert access_key is not None, 'Missing required parameter: access_key'
    assert url is not None, 'Missing required parameter: url'
    
    querystring = {'access_key': access_key, 'url': quote(url), 'viewport': viewport, 'user_agent': user_agent, 'accept_lang': accept_lang}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=True)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params={'access_key': access_key, 'url': quote(url)}, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = http_headers_capture(access_key='YOUR_ACCESS_KEY', url='http://tumblr.com', viewport='375x667', user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4', accept_lang='es-ES')
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