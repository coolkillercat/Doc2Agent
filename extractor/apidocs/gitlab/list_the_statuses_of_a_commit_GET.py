import requests, json
from urllib.parse import quote


def list_the_statuses_of_a_commit(id=None, sha=None, ref=None, stage=None, name=None, all=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(id, safe='')}/repository/commits/{quote(sha, safe='')}/statuses"
    querystring = {'id': id, 'sha': sha, 'ref': ref, 'stage': stage, 'name': name, 'all': all, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert sha is not None, 'Missing required parameter: sha'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_the_statuses_of_a_commit(id=17, sha='''18f3e63d05582537db6d183d9d557be09e1f90c8''', ref='''main''', stage='''test''', name='''bundler:audit''', all=False)
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

