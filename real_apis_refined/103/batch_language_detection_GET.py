import requests
from urllib.parse import quote
                
def batch_language_detection(access_key=None, query__=None):
    api_url = f"https://api.languagelayer.com/batch"
    
    # Convert list of queries to comma-separated string if it's a list
    if isinstance(query__, list):
        query__ = ','.join(query__)
    
    querystring = {'access_key': access_key, 'query': query__}
    assert access_key is not None, 'Missing required parameter: access_key'
    assert query__ is not None, 'Missing required parameter: query__'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = batch_language_detection(access_key='YOUR_ACCESS_KEY', query__=['Hello World', 'Hola Mundo', 'Hallo Welt'])
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