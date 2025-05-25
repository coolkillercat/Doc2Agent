import requests, json
from urllib.parse import quote


def list_project_pipelines(id=None, name=None, order_by=None, ref=None, scope=None, sha=None, sort=None, source=None, status=None, updated_after=None, updated_before=None, username=None, yaml_errors=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/pipelines"
    querystring = {'id': id, 'name': name, 'order_by': order_by, 'ref': ref, 'scope': scope, 'sha': sha, 'sort': sort, 'source': source, 'status': status, 'updated_after': updated_after, 'updated_before': updated_before, 'username': username, 'yaml_errors': yaml_errors, }
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
    r = list_project_pipelines(id=1, name='''Build pipeline''', order_by='''id''', ref='''main''', scope='''running''', sha='''a91957a858320c0e17f3a0eca7cfacbff50ea29a''', sort='''desc''', source='''push''', status='''success''', updated_after=2019-03-15T08:00:00Z, updated_before=2019-03-15T08:00:00Z, username='''root''', yaml_errors=false)
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

