import requests, json
from urllib.parse import quote


def create_a_feature_flag(id=None, name=None, version=None, description=None, active=None, strategies=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/feature_flags"
    payload = {'id': id, 'name': name, 'version': version, 'description': description, 'active': active, 'strategies': strategies, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    assert version is not None, 'Missing required parameter: version'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_feature_flag(id=1, name='''awesome_feature''', version='''new_version_flag''', description='''This is a feature flag for testing.''', active=True, strategies=[{ "name": "default", "parameters": {}, "scopes": [{ "environment_scope": "production" }] }])
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

