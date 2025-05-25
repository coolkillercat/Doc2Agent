import requests
from urllib.parse import quote
                
def check_gender_of_a_name(name=None, country_id=None, language_id=None):
    api_url = f"https://api.genderize.io"
    querystring = {'name': name, 'country_id': country_id, 'language_id': language_id, }
    assert name is not None, 'Missing required parameter: name'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = check_gender_of_a_name(name='''John''', country_id='''US''', language_id='''en''')
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

