import requests
from urllib.parse import quote
                
def set_key_value(key=None, value=None, namespace='default'):
    api_url = f"https://api.countapi.xyz/set/{namespace}/{quote(str(key), safe='')}"
    querystring = {'value': value}
    assert key is not None, 'Missing required parameter: key'
    assert value is not None, 'Missing required parameter: value'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50, verify=False) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = set_key_value(key='''test''', value=69, namespace='''mysite.com''')
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