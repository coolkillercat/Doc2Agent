import requests
from urllib.parse import quote
                
def generate_chart(cht=None, chd=None, chs=None, chl=None, chan=None, chf=None):
    api_url = f"https://image-charts.com/chart"
    querystring = {'cht': cht, 'chd': chd, 'chs': chs, 'chl': chl, 'chan': chan, 'chf': chf, }
    assert cht is not None, 'Missing required parameter: cht'
    assert chd is not None, 'Missing required parameter: chd'
    assert chs is not None, 'Missing required parameter: chs'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = generate_chart(cht='''p3''', chd='''t:60,40''', chs='''700x100''', chl='''Hello|World''', chan=True, chf='''ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1''')
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
    result_dict['content'] = r.content
    print(json.dumps(result_dict, indent=4, default=lambda x: x.decode('latin-1') if isinstance(x, bytes) else str(x)))