import requests
from urllib.parse import quote
                
def thumbnail_capture(access_key=None, url=None, viewport='1440x900', width=300):
    api_url = f"https://api.screenshotlayer.com/api/capture"
    assert access_key is not None, 'Missing required parameter: access_key'
    assert url is not None, 'Missing required parameter: url'
    
    # URL encode the url parameter
    encoded_url = quote(url)
    
    querystring = {'access_key': access_key, 'url': encoded_url, 'viewport': viewport, 'width': width}
    
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params={'access_key': access_key, 'url': encoded_url}, timeout=50)
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = thumbnail_capture(access_key='YOUR_ACCESS_KEY', url='http://amazon.com', viewport='1440x900', width=300)
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