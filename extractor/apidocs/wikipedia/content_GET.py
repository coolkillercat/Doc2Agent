import requests
from urllib.parse import quote
                
def content(ZIMNAME=None, PATH_IN_ZIMFILE=None):
    api_url = f"http://localhost:8080/content"
    querystring = {'ZIMNAME': ZIMNAME, 'PATH_IN_ZIMFILE': PATH_IN_ZIMFILE, }
    assert ZIMNAME is not None, 'Missing required parameter: ZIMNAME'
    assert PATH_IN_ZIMFILE is not None, 'Missing required parameter: PATH_IN_ZIMFILE'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = content(ZIMNAME='''exampleZIM''', PATH_IN_ZIMFILE='''path/to/content''')
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