import requests
from urllib.parse import quote
                
def get_custom_attribute(id=None, key=None):
    api_url = f"/api/v4/groups/{quote(id, safe='')}/custom_attributes/{quote(key, safe='')}"
    querystring = {'id': id, 'key': key, }
    assert id is not None, 'Missing required parameter: id'
    assert key is not None, 'Missing required parameter: key'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_custom_attribute(id='''123''', key='''attribute_key''')
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

