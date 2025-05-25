import requests, json
from urllib.parse import quote


def add_a_member_role_to_a_group(id=None, name=None, base_access_level=None, description=None, admin_merge_request=None, admin_terraform_state=None, admin_vulnerability=None, read_code=None, read_dependency=None, read_vulnerability=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/:id/member_roles"
    payload = {'id': id, 'name': name, 'base_access_level': base_access_level, 'description': description, 'admin_merge_request': admin_merge_request, 'admin_terraform_state': admin_terraform_state, 'admin_vulnerability': admin_vulnerability, 'read_code': read_code, 'read_dependency': read_dependency, 'read_vulnerability': read_vulnerability, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    assert base_access_level is not None, 'Missing required parameter: base_access_level'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_a_member_role_to_a_group(id=84, name='''Custom guest''', base_access_level=10, description='''Custom guest that can read code''', admin_merge_request=false, admin_terraform_state=false, admin_vulnerability=false, read_code=true, read_dependency=false, read_vulnerability=false)
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

