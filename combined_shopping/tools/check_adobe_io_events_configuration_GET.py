import requests
from urllib.parse import quote
                
<<<<<<<< HEAD:real_apis_refined/10/request_json_GET.py
def request_json(id=None):
    api_url = f"https://json.extendsclass.com/bin/{quote(id, safe='')}"
    querystring = {'id': id, }
    assert id is not None, 'Missing required parameter: id'
========
def check_adobe_io_events_configuration():
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/adobe_io_events/check_configuration"
    querystring = {}
>>>>>>>> 202136d56c7f13358750999b2a1612618966e779:combined_shopping/tools/check_adobe_io_events_configuration_GET.py
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
<<<<<<<< HEAD:real_apis_refined/10/request_json_GET.py
    r = request_json(id='''12345''')
========
    r = check_adobe_io_events_configuration()
>>>>>>>> 202136d56c7f13358750999b2a1612618966e779:combined_shopping/tools/check_adobe_io_events_configuration_GET.py
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

