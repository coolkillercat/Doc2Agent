import requests, json
from urllib.parse import quote


def list_project_iterations(id=None, state=None, search=None, in=None, include_ancestors=None, include_descendants=None, updated_before=None, updated_after=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/iterations"
    querystring = {'id': id, 'state': state, 'search': search, 'in': in, 'include_ancestors': include_ancestors, 'include_descendants': include_descendants, 'updated_before': updated_before, 'updated_after': updated_after, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_project_iterations(id=5, state='''opened''', search='''version''', in=['title'], include_ancestors=True, include_descendants=False, updated_before=2019-03-15T08:00:00Z, updated_after=2019-03-15T08:00:00Z)
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

