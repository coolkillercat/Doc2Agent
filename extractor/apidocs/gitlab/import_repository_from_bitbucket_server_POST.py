import requests, json
from urllib.parse import quote


def import_repository_from_bitbucket_server(bitbucket_server_url=None, bitbucket_server_username=None, personal_access_token=None, bitbucket_server_project=None, bitbucket_server_repo=None, new_name=None, target_namespace=None, timeout_strategy='pessimistic'):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/import/bitbucket_server"
    payload = {'bitbucket_server_url': bitbucket_server_url, 'bitbucket_server_username': bitbucket_server_username, 'personal_access_token': personal_access_token, 'bitbucket_server_project': bitbucket_server_project, 'bitbucket_server_repo': bitbucket_server_repo, 'new_name': new_name, 'target_namespace': target_namespace, 'timeout_strategy': timeout_strategy, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert bitbucket_server_url is not None, 'Missing required parameter: bitbucket_server_url'
    assert bitbucket_server_username is not None, 'Missing required parameter: bitbucket_server_username'
    assert personal_access_token is not None, 'Missing required parameter: personal_access_token'
    assert bitbucket_server_project is not None, 'Missing required parameter: bitbucket_server_project'
    assert bitbucket_server_repo is not None, 'Missing required parameter: bitbucket_server_repo'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = import_repository_from_bitbucket_server(bitbucket_server_url='''http://bitbucket.example.com''', bitbucket_server_username='''root''', personal_access_token='''Nzk4MDcxODY4MDAyOiP8y410zF3tGAyLnHRv/E0+3xYs''', bitbucket_server_project='''NEW''', bitbucket_server_repo='''my-repo''', new_name='''NEW-NAME''', target_namespace='''group/subgroup''', timeout_strategy='''optimistic''')
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

