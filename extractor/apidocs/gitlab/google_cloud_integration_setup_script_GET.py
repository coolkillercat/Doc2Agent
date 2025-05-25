import requests, json
from urllib.parse import quote


def google_cloud_integration_setup_script(id=None, enable_google_cloud_artifact_registry=None, google_cloud_artifact_registry_project_id=None):
    api_url = f"https://gitlab.com/api/v4/projects/{your_project_id}/google_cloud/setup/integrations.sh"
    querystring = {'id': id, 'enable_google_cloud_artifact_registry': enable_google_cloud_artifact_registry, 'google_cloud_artifact_registry_project_id': google_cloud_artifact_registry_project_id, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert enable_google_cloud_artifact_registry is not None, 'Missing required parameter: enable_google_cloud_artifact_registry'
    assert google_cloud_artifact_registry_project_id is not None, 'Missing required parameter: google_cloud_artifact_registry_project_id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = google_cloud_integration_setup_script(id=123, enable_google_cloud_artifact_registry=true, google_cloud_artifact_registry_project_id='''artifact-registry-project''')
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

