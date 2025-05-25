import requests
from urllib.parse import quote
                
def get_zip_codes(per_page=15, page=1, city=None, state=None, colony=None, zip_code=None):
    api_url = f"https://sepomex.icalialabs.com/api/v1/zip_codes"
    querystring = {'per_page': per_page, 'page': page, 'city': city, 'state': state, 'colony': colony, 'zip_code': zip_code, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_zip_codes(per_page=200, page=2, city='''monterrey''', state='''nuevo leon''', colony='''punta contry''', zip_code='''67173''')
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

