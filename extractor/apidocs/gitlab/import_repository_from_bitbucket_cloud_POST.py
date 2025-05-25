import requests, json
from urllib.parse import quote


def import_repository_from_bitbucket_cloud(bitbucket_username=None, bitbucket_app_password=None, repo_path=None, target_namespace=None, new_name=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/import/bitbucket"
    payload = {'bitbucket_username': bitbucket_username, 'bitbucket_app_password': bitbucket_app_password, 'repo_path': repo_path, 'target_namespace': target_namespace, 'new_name': new_name, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert bitbucket_username is not None, 'Missing required parameter: bitbucket_username'
    assert bitbucket_app_password is not None, 'Missing required parameter: bitbucket_app_password'
    assert repo_path is not None, 'Missing required parameter: repo_path'
    assert target_namespace is not None, 'Missing required parameter: target_namespace'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = import_repository_from_bitbucket_cloud(bitbucket_username='''bitbucket_username''', bitbucket_app_password='''bitbucket_app_password''', repo_path='''username/my_project''', target_namespace='''my_group/my_subgroup''', new_name='''new_project_name''')
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

