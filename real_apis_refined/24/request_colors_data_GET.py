import requests
from urllib.parse import quote
                
def request_colors_data(keyword=None, hex=None, rgb=None, rgba=None, hsl=None, hsla=None):
    api_url = f"https://color.serialif.com/"
    querystring = {'keyword': keyword, 'hex': hex, 'rgb': rgb, 'rgba': rgba, 'hsl': hsl, 'hsla': hsla, }
    assert keyword is not None, 'Missing required parameter: keyword'
    assert hex is not None, 'Missing required parameter: hex'
    assert rgb is not None, 'Missing required parameter: rgb'
    assert rgba is not None, 'Missing required parameter: rgba'
    assert hsl is not None, 'Missing required parameter: hsl'
    assert hsla is not None, 'Missing required parameter: hsla'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = request_colors_data(keyword='''aquamarine''', hex='''55667788''', rgb='''85,102,119''', rgba='''85,102,119,0.53''', hsl='''85,102,119''', hsla='''85,102,119,0.53''')
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

