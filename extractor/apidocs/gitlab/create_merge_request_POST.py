import requests, json
from urllib.parse import quote


def create_merge_request(id=None, source_branch=None, target_branch=None, title=None, description=None, assignee_id=None, labels=None, milestone_id=None, remove_source_branch=None, squash=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/merge_requests"
    payload = {'id': id, 'source_branch': source_branch, 'target_branch': target_branch, 'title': title, 'description': description, 'assignee_id': assignee_id, 'labels': labels, 'milestone_id': milestone_id, 'remove_source_branch': remove_source_branch, 'squash': squash, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert source_branch is not None, 'Missing required parameter: source_branch'
    assert target_branch is not None, 'Missing required parameter: target_branch'
    assert title is not None, 'Missing required parameter: title'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_merge_request(id=76, source_branch='''feature-branch''', target_branch='''main''', title='''Add new feature''', description='''This merge request adds a new feature.''', assignee_id=1, labels='''feature,urgent''', milestone_id=5, remove_source_branch=True, squash=True)
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

