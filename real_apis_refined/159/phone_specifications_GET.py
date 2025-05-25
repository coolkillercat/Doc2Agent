import requests
from urllib.parse import quote
                
def phone_specifications(brand_slug=None, phone_slug=None):
    api_url = f"https://api-mobilespecs.azharimm.dev/brands/{quote(brand_slug, safe='')}/phones/{quote(phone_slug, safe='')}"
    assert brand_slug is not None, 'Missing required parameter: brand_slug'
    assert phone_slug is not None, 'Missing required parameter: phone_slug'
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = phone_specifications(brand_slug='''apple''', phone_slug='''apple_iphone_12_pro_max-10237''')
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