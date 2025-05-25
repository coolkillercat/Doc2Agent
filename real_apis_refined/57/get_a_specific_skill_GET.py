import requests
from urllib.parse import quote

def get_a_specific_skill(idOrSlug=None, p=None):
    if isinstance(idOrSlug, int) or idOrSlug.isdigit():
        api_url = f"https://mhw-db.com/skills/{idOrSlug}"
    else:
        api_url = f"https://mhw-db.com/skills/{quote(str(idOrSlug))}"
    
    querystring = {'p': p}
    assert idOrSlug is not None, 'Missing required parameter: idOrSlug'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_a_specific_skill(idOrSlug='poison-resistance', p=None)
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