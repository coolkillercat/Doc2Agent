import requests
from urllib.parse import quote
                
def get_puns_by_searching(query=None):
    assert query is not None, 'Missing required parameter: query'
    
    api_url = "https://icanhazdadjoke.com/search"
    querystring = {'term': query}
    
    headers = {
        'Accept': 'application/json'
    }
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, headers=headers, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_puns_by_searching(query='cookie')
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