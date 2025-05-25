import requests
from urllib.parse import quote
                
def _words(ml=None, sl=None, sp=None, rel__code_=None, v=None, topics=None, lc=None, rc=None, max=None, md=None, qe=None):
    api_url = f"https://api.datamuse.com/words"
    querystring = {'ml': ml, 'sl': sl, 'sp': sp, 'rel__code_': rel__code_, 'v': v, 'topics': topics, 'lc': lc, 'rc': rc, 'max': max, 'md': md, 'qe': qe, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = _words(ml='''ringing in the ears''', sl='''jirraf''', sp='''hipopatamus''', rel__code_='''rel_jjb=ocean''', v='''enwiki''', topics='''temperature''', lc='''drink''', rc='''water''', max=100, md='''dpsr''', qe='''sp''')
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

