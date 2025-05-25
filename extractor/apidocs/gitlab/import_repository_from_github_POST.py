import requests, json
from urllib.parse import quote


def import_repository_from_github(personal_access_token=None, repo_id=None, target_namespace=None, new_name=None, github_hostname=None, optional_stages=None, timeout_strategy='pessimistic'):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/import/github"
    payload = {'personal_access_token': personal_access_token, 'repo_id': repo_id, 'target_namespace': target_namespace, 'new_name': new_name, 'github_hostname': github_hostname, 'optional_stages': optional_stages, 'timeout_strategy': timeout_strategy, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert personal_access_token is not None, 'Missing required parameter: personal_access_token'
    assert repo_id is not None, 'Missing required parameter: repo_id'
    assert target_namespace is not None, 'Missing required parameter: target_namespace'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = import_repository_from_github(personal_access_token='''aBc123abC12aBc123abC12abC123+_A/c123''', repo_id=12345, target_namespace='''group/subgroup''', new_name='''NEW-NAME''', github_hostname='''https://github.example.com''', optional_stages={'single_endpoint_notes_import': True, 'attachments_import': True, 'collaborators_import': True}, timeout_strategy='''optimistic''')
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

