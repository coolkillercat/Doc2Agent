import requests, json
from urllib.parse import quote


def list_group_milestones(id=None, iids__=None, state=None, title=None, search=None, include_ancestors=None, include_descendants=None, updated_before=None, updated_after=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/{quote(id, safe='')}/milestones"
    querystring = {'id': id, 'iids__': iids__, 'state': state, 'title': title, 'search': search, 'include_ancestors': include_ancestors, 'include_descendants': include_descendants, 'updated_before': updated_before, 'updated_after': updated_after, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_group_milestones(id=5, iids__=[42, 43], state='''active''', title='''1.0''', search='''version''', include_ancestors=true, include_descendants=true, updated_before=2013-10-02T09:24:18Z, updated_after=2013-10-02T09:24:18Z)
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

