import requests
from urllib.parse import quote
                
def invoke_assessment(host=None, hidden=None, rescan=None):
    api_url = f"https://http-observatory.security.mozilla.org/api/v1/analyze"
    payload = {'host': host, 'hidden': hidden, 'rescan': rescan, }
    assert host is not None, 'Missing required parameter: host'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = invoke_assessment(host='''www.mozilla.org''', hidden=True, rescan=True)
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

