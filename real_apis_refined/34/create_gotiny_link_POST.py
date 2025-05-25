import requests
from urllib.parse import quote
                
def create_gotiny_link(input=None, custom=None, useFallback=True):
    api_url = f"https://gotiny.cc/api"
    payload = {'input': input, 'custom': custom, 'useFallback': useFallback, }
    assert input is not None, 'Missing required parameter: input'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_gotiny_link(input='''https://amazon.com/very-long-url''', custom='''custom-link''', useFallback=False)
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

