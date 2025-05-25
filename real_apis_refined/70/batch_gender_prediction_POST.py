import requests
from urllib.parse import quote
                
def batch_gender_prediction(names=None, country_id=None, language_id=None):
    api_url = f"https://api.genderize.io"
    payload = {'names': names, 'country_id': country_id, 'language_id': language_id, }
    assert names is not None, 'Missing required parameter: names'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = batch_gender_prediction(names=['John', 'Jane'], country_id='''US''', language_id='''en''')
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

