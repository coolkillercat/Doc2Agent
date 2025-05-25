import requests
from urllib.parse import quote
                
def list_phones(brand_slug=None, page=1):
    api_url = f"https://api-mobilespecs.azharimm.dev/brands/{quote(brand_slug, safe='')}/phones"
    querystring = {'page': page}
    assert brand_slug is not None, 'Missing required parameter: brand_slug'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50, verify=False) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_phones(brand_slug='''apple-phones-48''', page=2)
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