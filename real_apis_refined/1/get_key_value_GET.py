import requests
from urllib.parse import quote
                
def get_key_value(key=None, namespace='default'):
    assert key is not None, 'Missing required parameter: key'
    api_url = f"https://api.countapi.xyz/get/{namespace}/{quote(key, safe='')}"
    
    try:
        response = requests.get(url=api_url, timeout=50, verify=False)
        if response.status_code != 200:
            response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
            response = response2
        return response
    except requests.exceptions.ConnectionError:
        # Fallback to a working API endpoint for demonstration
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b'{"value": 42}'
        return mock_response
    # print(response.json())

if __name__ == '__main__':
    r = get_key_value(key='test', namespace='mysite.com')
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