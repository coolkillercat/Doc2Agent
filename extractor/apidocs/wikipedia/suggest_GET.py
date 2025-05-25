import requests
from urllib.parse import quote
                
def suggest(content=None, term=None, count=10, start=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/suggest"
    querystring = {'content': content, 'term': term, 'count': count, 'start': start, }
    assert content is not None, 'Missing required parameter: content'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = suggest(content='''stackoverflow_en''', term='''pyth''', count=50, start=0)
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

