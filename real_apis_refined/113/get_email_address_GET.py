import requests
from urllib.parse import quote
                
def get_email_address(f=None, ip=None, agent=None, lang=None, SUBSCR=None):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    querystring = {'f': f, 'ip': ip, 'agent': agent, 'lang': lang, 'SUBSCR': SUBSCR, }
    assert f is not None, 'Missing required parameter: f'
    assert ip is not None, 'Missing required parameter: ip'
    assert agent is not None, 'Missing required parameter: agent'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_email_address(f='''get_email_address''', ip='''127.0.0.1''', agent='''Mozilla/5.0''', lang='''en''', SUBSCR='''SUBSCR=example_subscriber_data''')
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

