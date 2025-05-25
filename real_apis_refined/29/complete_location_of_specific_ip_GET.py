import requests
from urllib.parse import quote
                
def complete_location_of_specific_ip(ip=None, format='json'):
    api_url = f"https://ipapi.co/{quote(ip, safe='')}/{quote(format, safe='')}/"
    querystring = {'ip': ip, 'format': format, }
    assert ip is not None, 'Missing required parameter: ip'
    assert format is not None, 'Missing required parameter: format'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = complete_location_of_specific_ip(ip='''8.8.8.8''', format='''json''')
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

