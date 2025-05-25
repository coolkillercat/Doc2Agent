import requests, json
from urllib.parse import quote


def create_a_push_mirror(id=None, url=None, enabled=None, keep_divergent_refs=None, only_protected_branches=None, mirror_branch_regex=None, auth_method=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/remote_mirrors"
    payload = {'id': id, 'url': url, 'enabled': enabled, 'keep_divergent_refs': keep_divergent_refs, 'only_protected_branches': only_protected_branches, 'mirror_branch_regex': mirror_branch_regex, 'auth_method': auth_method, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert url is not None, 'Missing required parameter: url'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_push_mirror(id=42, url='''https://username:token@example.com/gitlab/example.git''', enabled=False, keep_divergent_refs=False, only_protected_branches=False, mirror_branch_regex='''feature/*''', auth_method='''password''')
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

