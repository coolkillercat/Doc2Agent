import requests
from urllib.parse import quote
                
def get_color_suggestions(input=None, model='default'):
    api_url = f"http://colormind.io/api/"
    payload = {'input': input, 'model': model, }
    assert input is not None, 'Missing required parameter: input'
    assert model is not None, 'Missing required parameter: model'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_color_suggestions(input=[[44,43,44],[90,83,82],'N','N','N'], model='''default''')
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

