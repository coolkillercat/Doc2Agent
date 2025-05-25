import requests
from urllib.parse import quote
                
def avatars(uuid=None, size=None, overlay=None, default='MHF_Steve or MHF_Alex'):
    api_url = f"https://crafatar.com/avatars/{quote(str(uuid), safe='')}"
    querystring = {}
    if size is not None:
        querystring['size'] = size
    if overlay is not None:
        querystring['overlay'] = overlay
    if default is not None:
        querystring['default'] = default
    assert uuid is not None, 'Missing required parameter: uuid'
    
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = avatars(uuid='''853c80ef3c3749fdaa49938b674adae6''', size=128, overlay=True, default='''MHF_Steve''')
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
    result_dict['content'] = r.content
    print(json.dumps(result_dict, indent=4, default=lambda x: x.decode('latin-1') if isinstance(x, bytes) else str(x)))