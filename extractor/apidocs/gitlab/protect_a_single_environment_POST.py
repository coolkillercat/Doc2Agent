import requests, json
from urllib.parse import quote


def protect_a_single_environment(id=None, name=None, deploy_access_levels=None, approval_rules=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/protected_environments"
    payload = {'id': id, 'name': name, 'deploy_access_levels': deploy_access_levels, 'approval_rules': approval_rules, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    assert deploy_access_levels is not None, 'Missing required parameter: deploy_access_levels'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = protect_a_single_environment(id=22034114, name='''production''', deploy_access_levels=[{"group_id": 9899826}], approval_rules=[{"group_id": 134, "required_approvals": 2}])
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

