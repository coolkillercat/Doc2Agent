import requests
from urllib.parse import quote
                
def get_verse(editionName=None, ChapterNo=None, VerseNo=None):
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{quote(str(editionName), safe='')}/{quote(str(ChapterNo), safe='')}/{quote(str(VerseNo), safe='')}.json"
    querystring = {'editionName': editionName, 'ChapterNo': ChapterNo, 'VerseNo': VerseNo, }
    assert editionName is not None, 'Missing required parameter: editionName'
    assert ChapterNo is not None, 'Missing required parameter: ChapterNo'
    assert VerseNo is not None, 'Missing required parameter: VerseNo'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_verse(editionName='''ben-muhiuddinkhan''', ChapterNo=5, VerseNo=10)
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