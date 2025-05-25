import requests, json
from urllib.parse import quote


def set_the_pipeline_status_of_a_commit(id=None, sha=None, state=None, ref=None, name_or_context=None, target_url=None, description=None, coverage=None, pipeline_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/statuses/:sha"
    payload = {'id': id, 'sha': sha, 'state': state, 'ref': ref, 'name_or_context': name_or_context, 'target_url': target_url, 'description': description, 'coverage': coverage, 'pipeline_id': pipeline_id, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert sha is not None, 'Missing required parameter: sha'
    assert state is not None, 'Missing required parameter: state'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = set_the_pipeline_status_of_a_commit(id=17, sha='''18f3e63d05582537db6d183d9d557be09e1f90c8''', state='''success''', ref='''main''', name_or_context='''default''', target_url='''https://example.com/build/status''', description='''Build succeeded''', coverage=100.0, pipeline_id=123)
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

