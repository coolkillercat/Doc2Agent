import requests
from urllib.parse import quote
                
def reverse_dns_lookup_for_cidr_range(ip=None, mask=None):
    api_url = f"https://sonar.omnisint.io/reverse/{quote(ip, safe='')}/{quote(mask, safe='')}"
    querystring = {'ip': ip, 'mask': mask, }
    assert ip is not None, 'Missing required parameter: ip'
    assert mask is not None, 'Missing required parameter: mask'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = reverse_dns_lookup_for_cidr_range(ip='''8.8.8.0''', mask='''24''')
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

