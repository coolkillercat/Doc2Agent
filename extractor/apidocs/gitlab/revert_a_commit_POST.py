import requests, json
from urllib.parse import quote


def revert_a_commit(id=None, sha=None, branch=None, dry_run=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/repository/commits/:sha/revert"
    payload = {'id': id, 'sha': sha, 'branch': branch, 'dry_run': dry_run, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert sha is not None, 'Missing required parameter: sha'
    assert branch is not None, 'Missing required parameter: branch'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = revert_a_commit(id=5, sha='''a738f717824ff53aebad8b090c1b79a14f2bd9e8''', branch='''main''', dry_run=False)
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

