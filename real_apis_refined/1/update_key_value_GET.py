import requests
from urllib.parse import quote
                
def update_key_value(key=None, amount=None, namespace='default'):
    api_url = f"https://api.countapi.xyz/update/{namespace}/{quote(str(key), safe='')}"
    querystring = {'amount': amount}
    assert key is not None, 'Missing required parameter: key'
    assert amount is not None, 'Missing required parameter: amount'
    
    try:
        response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
        if response.status_code != 200:
            response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
            response = response2
        return response
    except requests.exceptions.ConnectionError:
        # Fallback to alternative API endpoint
        api_url = f"https://api.countapi.com/update/{namespace}/{quote(str(key), safe='')}"
        response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
        return response
    # print(response.json())

if __name__ == '__main__':
    r = update_key_value(key='''test''', amount=5, namespace='''mysite.com''')
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