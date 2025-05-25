import requests, json
from urllib.parse import quote


def list_group_iterations(id=None, state=None, search=None, in=None, include_ancestors=None, include_descendants=None, updated_before=None, updated_after=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(id, safe='')}/iterations"
    querystring = {'id': id, 'state': state, 'search': search, 'in': in, 'include_ancestors': include_ancestors, 'include_descendants': include_descendants, 'updated_before': updated_before, 'updated_after': updated_after, }
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
    r = list_group_iterations(id='''5''', state='''opened''', search='''version''', in=["title"], include_ancestors=true, include_descendants=true, updated_before=2013-10-02T09:24:18Z, updated_after=2013-10-02T09:24:18Z)
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

