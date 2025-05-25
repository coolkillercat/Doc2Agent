import requests
from urllib.parse import quote
                
def specific_location_field_of_specific_ip(ip=None, field=None):
    api_url = f"https://ipapi.co/{quote(ip, safe='')}/{quote(field, safe='')}/"
    querystring = {'ip': ip, 'field': field, }
    assert ip is not None, 'Missing required parameter: ip'
    assert field is not None, 'Missing required parameter: field'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = specific_location_field_of_specific_ip(ip='''8.8.8.8''', field='''country''')
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

