import requests, json
from urllib.parse import quote


def create_a_deployment(id=None, environment=None, sha=None, ref=None, tag=None, status=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/deployments"
    payload = {'id': id, 'environment': environment, 'sha': sha, 'ref': ref, 'tag': tag, 'status': status, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert environment is not None, 'Missing required parameter: environment'
    assert sha is not None, 'Missing required parameter: sha'
    assert ref is not None, 'Missing required parameter: ref'
    assert tag is not None, 'Missing required parameter: tag'
    assert status is not None, 'Missing required parameter: status'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_deployment(id=1, environment='''production''', sha='''a91957a858320c0e17f3a0eca7cfacbff50ea29a''', ref='''main''', tag=False, status='''success''')
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

