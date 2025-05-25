import requests, json
from urllib.parse import quote


def set_or_create_a_feature(name=None, value=None, key=None, feature_group=None, user=None, group=None, namespace=None, project=None, repository=None, force=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/features/:name"
    payload = {'name': name, 'value': value, 'key': key, 'feature_group': feature_group, 'user': user, 'group': group, 'namespace': namespace, 'project': project, 'repository': repository, 'force': force, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert name is not None, 'Missing required parameter: name'
    assert value is not None, 'Missing required parameter: value'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = set_or_create_a_feature(name='''new_feature''', value=true, key='''percentage_of_time''', feature_group='''group::ci''', user='''john_doe''', group='''gitlab-org''', namespace='''john-doe''', project='''gitlab-org/gitlab-foss''', repository='''gitlab-org/gitlab-test.git''', force=false)
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

