import requests
from urllib.parse import quote
                
def album_url_endpoint(query=None, lyrics=None):
    api_url = "https://jiosaavn-api-privatecvc2.vercel.app/albums"
    querystring = {"link": query}
    if lyrics is not None:
        querystring['lyrics'] = lyrics
    assert query is not None, 'Missing required parameter: query'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = album_url_endpoint(query='''https://www.jiosaavn.com/album/chhichhore/V4F3M5,cNb4''', lyrics=True)
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