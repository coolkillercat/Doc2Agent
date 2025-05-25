import requests, json
from urllib.parse import quote


def runner_provisioning_configuration_script(id=None, google_cloud_project_id=None):
    api_url = f"https://gitlab.com/api/v4/projects/{your_project_id}/google_cloud/setup/runner_deployment_project.sh"
    querystring = {'id': id, 'google_cloud_project_id': google_cloud_project_id, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert google_cloud_project_id is not None, 'Missing required parameter: google_cloud_project_id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = runner_provisioning_configuration_script(id=123, google_cloud_project_id='''my-gcp-project''')
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

