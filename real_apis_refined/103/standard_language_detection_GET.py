import requests
from urllib.parse import quote
                
def standard_language_detection(access_key=None, query=None):
    api_url = f"https://api.apilayer.com/language_detection/detect"
    headers = {
        "apikey": access_key
    }
    querystring = {'query': query}
    assert access_key is not None, 'Missing required parameter: access_key'
    assert query is not None, 'Missing required parameter: query'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = standard_language_detection(access_key='''YOUR_ACCESS_KEY''', query='''Hello World''')
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