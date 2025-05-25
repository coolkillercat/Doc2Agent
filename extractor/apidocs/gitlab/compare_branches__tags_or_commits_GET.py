import requests, json
from urllib.parse import quote


def compare_branches__tags_or_commits(id=None, from=None, to=None, from_project_id=None, straight=None, unidiff=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/repository/compare"
    querystring = {'id': id, 'from': from, 'to': to, 'from_project_id': from_project_id, 'straight': straight, 'unidiff': unidiff, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert from is not None, 'Missing required parameter: from'
    assert to is not None, 'Missing required parameter: to'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = compare_branches__tags_or_commits(id=123, from='''main''', to='''feature''', from_project_id=456, straight=True, unidiff=True)
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

