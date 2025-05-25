import requests, json
from urllib.parse import quote


def create_project_level_approval_rule(id=None, approvals_required=None, name=None, applies_to_all_protected_branches=None, group_ids=None, protected_branch_ids=None, report_type=None, rule_type=None, user_ids=None, usernames=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/approval_rules"
    payload = {'id': id, 'approvals_required': approvals_required, 'name': name, 'applies_to_all_protected_branches': applies_to_all_protected_branches, 'group_ids': group_ids, 'protected_branch_ids': protected_branch_ids, 'report_type': report_type, 'rule_type': rule_type, 'user_ids': user_ids, 'usernames': usernames, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert approvals_required is not None, 'Missing required parameter: approvals_required'
    assert name is not None, 'Missing required parameter: name'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_project_level_approval_rule(id=1, approvals_required=2, name='''security''', applies_to_all_protected_branches=false, group_ids=[1, 2, 3], protected_branch_ids=[1, 2], report_type='''code_coverage''', rule_type='''regular''', user_ids=[123, 456], usernames=["jdoe", "group_member_1"])
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

