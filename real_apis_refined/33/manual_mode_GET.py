import requests
from urllib.parse import quote
                
def manual_mode(lang=None, ip=None, cc=None):
    api_url = f"https://hellosalut.stefanbohacek.dev/"
    querystring = {'lang': lang, 'ip': ip, 'cc': cc, }
    assert lang is not None, 'Missing required parameter: lang'
    assert ip is not None, 'Missing required parameter: ip'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = manual_mode(lang='''en''', ip='''89.120.120.120''', cc='''nl''')
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

