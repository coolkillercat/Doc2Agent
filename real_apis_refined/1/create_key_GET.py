import requests
from urllib.parse import quote
                
def create_key(name='New UUID', namespace='default', value=None, enable_reset=None, update_lowerbound=-1, update_upperbound=1):
    api_url = f"https://api.countapi.xyz/create"
    querystring = {'name': name, 'namespace': namespace, 'value': value, 'enable_reset': enable_reset, 'update_lowerbound': update_lowerbound, 'update_upperbound': update_upperbound, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_key(name='''counter''', namespace='''mysite.com''', value=42, enable_reset=True, update_lowerbound=-5, update_upperbound=5)
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