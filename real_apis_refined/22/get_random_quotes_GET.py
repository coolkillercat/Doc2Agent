import requests
from urllib.parse import quote
                
def get_random_quotes(limit=1, maxLength=None, minLength=None, tags=None, author=None, authorId=None):
    api_url = "https://api.quotable.io/quotes/random"
    querystring = {}
    
    # Only add non-None parameters to the query
    if limit is not None:
        querystring['limit'] = limit
    if maxLength is not None:
        querystring['maxLength'] = maxLength
    if minLength is not None:
        querystring['minLength'] = minLength
    if tags is not None:
        querystring['tags'] = tags
    if author is not None:
        querystring['author'] = author
    if authorId is not None:
        querystring['authorId'] = authorId
    
    try:
        response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
        if response.status_code != 200:
            response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
            response = response2
        return response
    except requests.exceptions.ConnectionError:
        # Fallback to a different API endpoint if the main one fails
        backup_api_url = "https://api.quotable.io/random"
        response = requests.get(url=backup_api_url, timeout=50, verify=False)
        return response
    # print(response.json())

if __name__ == '__main__':
    r = get_random_quotes(limit=5, maxLength=100, minLength=50, tags='technology,famous-quotes', author='albert-einstein', authorId='12345')
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