import requests
from urllib.parse import quote
                
def get_joke(Category__ies=None, format='json', blacklistFlags=None, lang='en', idRange=None, contains=None, type=None, amount=1):
    if Category__ies is None:
        Category__ies = "Any"
    
    api_url = f"https://v2.jokeapi.dev/joke/{Category__ies}"
    
    querystring = {}
    if format != 'json':
        querystring['format'] = format
    if blacklistFlags:
        querystring['blacklistFlags'] = blacklistFlags
    if lang != 'en':
        querystring['lang'] = lang
    if idRange:
        querystring['idRange'] = idRange
    if contains:
        querystring['contains'] = contains
    if type:
        querystring['type'] = type
    if amount != 1:
        querystring['amount'] = amount
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_joke(Category__ies='''Programming,Misc''', format='''xml''', blacklistFlags='''nsfw,sexist''', lang='''ru''', idRange='''0-55''', contains='''C#''', type='''twopart''', amount=5)
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