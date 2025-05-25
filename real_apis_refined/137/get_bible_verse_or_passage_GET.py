import requests
from urllib.parse import quote
                
def get_bible_verse_or_passage(BOOK=None, CHAPTER=None, VERSE=None, translation='web', verse_numbers=None, callback=None, random=None):
    api_url = f"https://bible-api.com/BOOK+CHAPTER:VERSE"
    querystring = {'BOOK': BOOK, 'CHAPTER': CHAPTER, 'VERSE': VERSE, 'translation': translation, 'verse_numbers': verse_numbers, 'callback': callback, 'random': random, }
    assert BOOK is not None, 'Missing required parameter: BOOK'
    assert CHAPTER is not None, 'Missing required parameter: CHAPTER'
    assert VERSE is not None, 'Missing required parameter: VERSE'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_bible_verse_or_passage(BOOK='''john''', CHAPTER=3, VERSE='''16''', translation='''kjv''', verse_numbers=True, callback='''func''', random='''verse''')
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

