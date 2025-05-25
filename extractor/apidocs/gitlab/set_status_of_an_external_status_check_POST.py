import requests, json
from urllib.parse import quote


def set_status_of_an_external_status_check(id=None, merge_request_iid=None, sha=None, external_status_check_id=None, status=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/merge_requests/:merge_request_iid/status_check_responses"
    payload = {'id': id, 'merge_request_iid': merge_request_iid, 'sha': sha, 'external_status_check_id': external_status_check_id, 'status': status, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    assert sha is not None, 'Missing required parameter: sha'
    assert external_status_check_id is not None, 'Missing required parameter: external_status_check_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = set_status_of_an_external_status_check(id=1, merge_request_iid=4, sha='''141be9714669a4c1ccaa013c6a7f3e462ff2a40f''', external_status_check_id=2, status='''passed''')
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

