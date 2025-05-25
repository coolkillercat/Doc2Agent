import requests, json
from urllib.parse import quote


def add_a_merge_request_to_a_merge_train(id=None, merge_request_iid=None, sha=None, squash=None, when_pipeline_succeeds=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/merge_trains/merge_requests/:merge_request_iid"
    payload = {'id': id, 'merge_request_iid': merge_request_iid, 'sha': sha, 'squash': squash, 'when_pipeline_succeeds': when_pipeline_succeeds, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_a_merge_request_to_a_merge_train(id=597, merge_request_iid=1, sha='''b83d6e391c22777fca1ed3012fce84f633d7fed0''', squash=true, when_pipeline_succeeds=true)
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

