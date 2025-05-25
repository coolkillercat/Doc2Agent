import requests, json
from urllib.parse import quote


def create_an_issue_link(id=None, issue_iid=None, target_project_id=None, target_issue_iid=None, link_type='relates_to'):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/issues/:issue_iid/links"
    payload = {'id': id, 'issue_iid': issue_iid, 'target_project_id': target_project_id, 'target_issue_iid': target_issue_iid, 'link_type': link_type, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert issue_iid is not None, 'Missing required parameter: issue_iid'
    assert target_project_id is not None, 'Missing required parameter: target_project_id'
    assert target_issue_iid is not None, 'Missing required parameter: target_issue_iid'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_an_issue_link(id=4, issue_iid=1, target_project_id=5, target_issue_iid=1, link_type='''relates_to''')
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

