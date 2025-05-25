import requests, json
from urllib.parse import quote


def validate_project_s_ci_configuration(content_ref='SHA of the head of the project's default branch', dry_run_ref='project's default branch', dry_run=None, include_jobs=None, ref='project's default branch', sha='SHA of the head of the project's default branch'):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/ci/lint"
    querystring = {'content_ref': content_ref, 'dry_run_ref': dry_run_ref, 'dry_run': dry_run, 'include_jobs': include_jobs, 'ref': ref, 'sha': sha, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = validate_project_s_ci_configuration(content_ref='''main''', dry_run_ref='''main''', dry_run=False, include_jobs=False, ref='''main''', sha='''main''')
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

