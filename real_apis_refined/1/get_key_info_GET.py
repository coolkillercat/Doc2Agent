import requests
from urllib.parse import quote
                
def get_key_info(key=None, namespace='default'):
    assert key is not None, 'Missing required parameter: key'
    api_url = f"https://api.countapi.com/info/{namespace}/{quote(key, safe='')}"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_key_info(key='test', namespace='mysite.com')
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