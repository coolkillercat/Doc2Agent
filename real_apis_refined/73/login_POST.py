import requests
from urllib.parse import quote
                
def login(action=None, lgname=None, lgpassword=None, format='json'):
    api_url = f"https://www.example.org/w/api.php"
    payload = {'action': action, 'lgname': lgname, 'lgpassword': lgpassword, 'format': format, }
    assert action is not None, 'Missing required parameter: action'
    assert lgname is not None, 'Missing required parameter: lgname'
    assert lgpassword is not None, 'Missing required parameter: lgpassword'
    assert format is not None, 'Missing required parameter: format'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = login(action='''login''', lgname='''user''', lgpassword='''password123''', format='''json''')
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

