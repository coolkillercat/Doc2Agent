import requests
from urllib.parse import quote
                
def generate_bacon_ipsum_text(type='meat-and-filler', paras=5, sentences=None, start_with_lorem=None, format='json'):
    api_url = f"https://baconipsum.com/api/"
    querystring = {'type': type, 'paras': paras, 'sentences': sentences, 'start_with_lorem': start_with_lorem, 'format': format, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = generate_bacon_ipsum_text(type='''all-meat''', paras=3, sentences=1, start_with_lorem=1, format='''html''')
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

