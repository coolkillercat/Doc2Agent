import requests
from urllib.parse import quote
                
def geoparsing(scantext=None, geoit='html', auth=None, sentiment=None):
    api_url = f"https://geocode.xyz"
    payload = {'scantext': scantext, 'geoit': geoit, 'auth': auth, 'sentiment': sentiment, }
    assert scantext is not None, 'Missing required parameter: scantext'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = geoparsing(scantext='''The most important museums of Amsterdam are located on the Museumplein, located at the southwestern side of the Rijksmuseum.''', geoit='''json''', auth='''your_api_key''', sentiment=1)
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

