import requests
from urllib.parse import quote
                
def field_options(connection_id=None, type=None, type_id=None, user_id=None):
    api_url = f"https://connect.ifttt.com/v2/connections/{{quote(connection_id, safe='')}}/{{quote(type, safe='')}}/{{quote(type_id, safe='')}}/field_options"
    querystring = {'connection_id': connection_id, 'type': type, 'type_id': type_id, 'user_id': user_id, }
    assert connection_id is not None, 'Missing required parameter: connection_id'
    assert type is not None, 'Missing required parameter: type'
    assert type_id is not None, 'Missing required parameter: type_id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = field_options(connection_id='''C8p3q9T6''', type='''actions''', type_id='''acme_cloud_storage.archive''', user_id='''123''')
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

