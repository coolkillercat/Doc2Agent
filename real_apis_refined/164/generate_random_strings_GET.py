import requests
from urllib.parse import quote
                
def generate_random_strings(len=10, count=1):
    api_url = "https://www.random.org/strings/"
    querystring = {
        'num': count,
        'len': len,
        'digits': 'on',
        'upperalpha': 'on',
        'loweralpha': 'on',
        'unique': 'on',
        'format': 'plain',
        'rnd': 'new'
    }
    
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response

if __name__ == '__main__':
    r = generate_random_strings(len=20, count=10)
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