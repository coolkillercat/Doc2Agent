import requests
from urllib.parse import quote
                
def list_quotes(maxLength=None, minLength=None, tags=None, author=None, authorId=None, sortBy="dateAdded", order="asc", limit=20, page=1):
    api_url = f"https://api.quotable.io/quotes"
    querystring = {'maxLength': maxLength, 'minLength': minLength, 'tags': tags, 'author': author, 'authorId': authorId, 'sortBy': sortBy, 'order': order, 'limit': limit, 'page': page, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_quotes(maxLength=100, minLength=50, tags='''technology,famous-quotes''', author='''albert-einstein''', authorId='''12345''', sortBy="author", order="desc", limit=50, page=2)
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