import requests
from urllib.parse import quote
                
def create_account(action=None, username=None, password=None, retype=None, createtoken=None, format='json'):
    api_url = f"https://www.example.org/w/api.php"
    payload = {'action': action, 'username': username, 'password': password, 'retype': retype, 'createtoken': createtoken, 'format': format, }
    assert action is not None, 'Missing required parameter: action'
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    assert retype is not None, 'Missing required parameter: retype'
    assert createtoken is not None, 'Missing required parameter: createtoken'
    assert format is not None, 'Missing required parameter: format'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_account(action='''createaccount''', username='''newuser''', password='''password123''', retype='''password123''', createtoken='''123ABC''', format='''json''')
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

