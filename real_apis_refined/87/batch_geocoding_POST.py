import requests
from urllib.parse import quote
                
def batch_geocoding(locate=None, geoit='html', auth=None):
    api_url = f"https://geocode.xyz"
    payload = {'locate': locate, 'geoit': geoit, 'auth': auth, }
    assert locate is not None, 'Missing required parameter: locate'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = batch_geocoding(locate='''input.csv''', geoit='''csv''', auth='''your_api_key''')
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

