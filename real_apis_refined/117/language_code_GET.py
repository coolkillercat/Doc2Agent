import requests
from urllib.parse import quote
                
def language_code(Language=None, format='json', lang='en'):
    api_url = f"https://v2.jokeapi.dev/langcode/[Language]"
    querystring = {'Language': Language, 'format': format, 'lang': lang, }
    assert Language is not None, 'Missing required parameter: Language'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = language_code(Language='''german''', format='''xml''', lang='''ru''')
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

