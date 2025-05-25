import requests, json
from urllib.parse import quote


def project_search_api(id=None, scope=None, search=None, confidential=None, ref=None, order_by=None, sort=None, state=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(id, safe='')}/search"
    querystring = {'id': id, 'scope': scope, 'search': search, 'confidential': confidential, 'ref': ref, 'order_by': order_by, 'sort': sort, 'state': state, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert scope is not None, 'Missing required parameter: scope'
    assert search is not None, 'Missing required parameter: search'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = project_search_api(id=12, scope='''issues''', search='''file''', confidential=False, ref='''main''', order_by='''created_at''', sort='''desc''', state='''opened''')
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

