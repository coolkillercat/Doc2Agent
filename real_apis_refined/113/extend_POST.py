import requests
from urllib.parse import quote
                
def extend(f=None, ip=None, agent=None):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    payload = {'f': f, 'ip': ip, 'agent': agent, }
    assert f is not None, 'Missing required parameter: f'
    assert ip is not None, 'Missing required parameter: ip'
    assert agent is not None, 'Missing required parameter: agent'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = extend(f='''extend''', ip='''127.0.0.1''', agent='''Mozilla/5.0''')
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

