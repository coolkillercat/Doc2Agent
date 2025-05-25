import requests
from urllib.parse import quote
                
def single_state_metadata(state_code=None):
    assert state_code is not None, 'Missing required parameter: state_code'
    state_code = state_code.lower()
    api_url = f"https://api.covidtracking.com/v1/states/{state_code}/info.json"
    
    response = requests.get(url=api_url, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = single_state_metadata(state_code='''mi''')
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