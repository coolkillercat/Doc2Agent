import requests
from urllib.parse import quote
                
def threads(id=None, minarticleid=None, minarticledate=None, count=None, username=None):
    api_url = "https://boardgamegeek.com/xmlapi2/thread"
    querystring = {'id': id, 'minarticleid': minarticleid, 'minarticledate': minarticledate, 'count': count, 'username': username}
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = threads(id=123, minarticleid=100, minarticledate='2023-01-01', count=10, username='john_doe')
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