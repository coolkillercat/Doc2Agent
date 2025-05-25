import requests
from urllib.parse import quote
                
def show_package(id=None):
    api_url = f"https://data.gov.ie/api/3/action/package_show"
    assert id is not None, 'Missing required parameter: id'
    
    querystring = {'name_or_id': id}
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, params={'id': id}, timeout=50, verify=False) # try with 'id' parameter
        if response2.status_code == 200:
            response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = show_package(id='the-walled-towns-of-ireland')
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