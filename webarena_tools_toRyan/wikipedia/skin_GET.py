import requests
from urllib.parse import quote
                
def skin(PATH_TO_RESOURCE=None, cacheid=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8888/skin"
    
    if PATH_TO_RESOURCE:
        api_url = f"{api_url}/{PATH_TO_RESOURCE}"
    
    querystring = {}
    if cacheid:
        querystring['cacheid'] = cacheid
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = skin(PATH_TO_RESOURCE='css/style.css', cacheid='12345')
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