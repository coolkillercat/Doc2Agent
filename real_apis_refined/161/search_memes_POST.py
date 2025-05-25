import requests
from urllib.parse import quote
                
def search_memes(username=None, password=None, query=None, include_nsfw=None):
    api_url = f"https://api.imgflip.com/search_memes"
    payload = {'username': username, 'password': password, 'q': query}
    if include_nsfw is not None:
        payload['nsfw'] = include_nsfw
    assert username is not None, 'Missing required parameter: username'
    assert password is not None, 'Missing required parameter: password'
    assert query is not None, 'Missing required parameter: query'
    
    response = requests.get(url=api_url, params=payload, timeout=50)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = search_memes(username='user123', password='password123', query='funny', include_nsfw=False)
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