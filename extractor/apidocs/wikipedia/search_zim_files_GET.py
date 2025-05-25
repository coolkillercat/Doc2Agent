import requests
from urllib.parse import quote
                
def search_zim_files(books_id=None, books_name=None, pattern=None, latitude=None, longitude=None, distance=None):
    api_url = "https://search.kiwix.org/search"
    querystring = {'books_id': books_id, 'books_name': books_name, 'pattern': pattern, 'latitude': latitude, 'longitude': longitude, 'distance': distance}
    assert books_id is not None, 'Missing required parameter: books_id'
    assert books_name is not None, 'Missing required parameter: books_name'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = search_zim_files(books_id='''123e4567-e89b-12d3-a456-426614174000''', books_name='''Wikipedia_en_all''', pattern='''Kiwix''', latitude=48.8588443, longitude=2.2943506, distance=1000)
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