import requests
from urllib.parse import quote
                
def github_gist_pins(id=None, show_owner=None):
    api_url = f"https://github-readme-stats.vercel.app/api/gist"
    querystring = {'id': id, 'show_owner': show_owner, }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = github_gist_pins(id='''bbfce31e0217a3689c8d961a356cb10d''', show_owner=True)
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

