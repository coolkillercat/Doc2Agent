import requests
from urllib.parse import quote
                
def json_response(text=None, add=None, fill_text='*', fill_char='*'):
    api_url = f"https://www.purgomalum.com/service/json"
    querystring = {'text': text, 'add': add, 'fill_text': fill_text, 'fill_char': fill_char, }
    assert text is not None, 'Missing required parameter: text'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = json_response(text='''this is some test input''', add='''input''', fill_text='''[replaced]''', fill_char='''_''')
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

