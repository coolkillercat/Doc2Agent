import requests
from urllib.parse import quote
                
def view_valid_results(session=None, download=None, separator='new-line'):
    api_url = f"https://www.disify.com/api/view/d117271ce938bf91bc718f6cfb7954de"
    querystring = {'session': session, 'download': download, 'separator': separator, }
    assert session is not None, 'Missing required parameter: session'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = view_valid_results(session='''d117271ce938bf91bc718f6cfb7954de''', download=True, separator='''comma''')
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

