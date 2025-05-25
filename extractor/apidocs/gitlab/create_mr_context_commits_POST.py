import requests, json
from urllib.parse import quote


def create_mr_context_commits(id=None, merge_request_iid=None, commits=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/merge_requests/:merge_request_iid/context_commits"
    payload = {'id': id, 'merge_request_iid': merge_request_iid, 'commits': commits, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    assert commits is not None, 'Missing required parameter: commits'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_mr_context_commits(id=15, merge_request_iid=12, commits=['51856a574ac3302a95f82483d6c7396b1e0783cb'])
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

