import requests
from urllib.parse import quote
                
def lookup_icelandic_addresses(address=None):
    api_url = "https://apis.is/isjakvottord"
    assert address is not None, 'Missing required parameter: address'
    
    querystring = {'address': address}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50, verify=False) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = lookup_icelandic_addresses(address='''laugavegur 1''')
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