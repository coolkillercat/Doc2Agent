import requests
from urllib.parse import quote
                
def submit_joke(formatVersion=None, category=None, type=None, joke=None, setup=None, delivery=None, flags=None, lang='en', dry_run=None):
    api_url = f"https://v2.jokeapi.dev/submit"
    payload = {'formatVersion': formatVersion, 'category': category, 'type': type, 'joke': joke, 'setup': setup, 'delivery': delivery, 'flags': flags, 'lang': lang, 'dry_run': dry_run, }
    assert formatVersion is not None, 'Missing required parameter: formatVersion'
    assert category is not None, 'Missing required parameter: category'
    assert type is not None, 'Missing required parameter: type'
    assert joke is not None, 'Missing required parameter: joke'
    assert setup is not None, 'Missing required parameter: setup'
    assert delivery is not None, 'Missing required parameter: delivery'
    assert flags is not None, 'Missing required parameter: flags'
    assert lang is not None, 'Missing required parameter: lang'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = submit_joke(formatVersion=3, category='''Misc''', type='''single''', joke='''A horse walks into a bar...''', setup='''Why do programmers wear glasses?''', delivery='''Because they need to C#''', flags={'nsfw': True, 'religious': False, 'political': True, 'racist': False, 'sexist': False, 'explicit': False}, lang='''en''', dry_run=True)
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

