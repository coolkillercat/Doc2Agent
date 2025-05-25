import requests
from urllib.parse import quote
                
def full_height_capture(access_key=None, url=None, viewport='2560x1440', fullpage=True):
    api_url = f"https://api.screenshotlayer.com/api/capture"
    querystring = {'access_key': access_key, 'url': url, 'viewport': viewport, 'fullpage': str(fullpage).lower()}
    assert access_key is not None, 'Missing required parameter: access_key'
    assert url is not None, 'Missing required parameter: url'
    
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params={'access_key': access_key, 'url': url}, timeout=50)
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = full_height_capture(access_key='YOUR_ACCESS_KEY', url='http://facebook.com', viewport='2560x1440', fullpage=True)
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