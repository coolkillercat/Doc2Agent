import requests
from urllib.parse import quote
                
def query_url_information_by_id(id=None):
    api_url = f"https://urlhaus-api.abuse.ch/v1/urlid/"
    payload = {'id': id, }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = query_url_information_by_id(id='''233833''')
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

