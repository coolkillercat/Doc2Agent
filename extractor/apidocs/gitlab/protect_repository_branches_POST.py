import requests, json
from urllib.parse import quote


def protect_repository_branches(id=None, name=None, allow_force_push=None, allowed_to_merge=None, allowed_to_push=None, allowed_to_unprotect=None, code_owner_approval_required=None, merge_access_level=None, push_access_level=None, unprotect_access_level=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/protected_branches"
    payload = {'id': id, 'name': name, 'allow_force_push': allow_force_push, 'allowed_to_merge': allowed_to_merge, 'allowed_to_push': allowed_to_push, 'allowed_to_unprotect': allowed_to_unprotect, 'code_owner_approval_required': code_owner_approval_required, 'merge_access_level': merge_access_level, 'push_access_level': push_access_level, 'unprotect_access_level': unprotect_access_level, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = protect_repository_branches(id=5, name='''*-stable''', allow_force_push=false, allowed_to_merge=[{"access_level": 30}], allowed_to_push=[{"access_level": 30}], allowed_to_unprotect=[{"access_level": 40}], code_owner_approval_required=false, merge_access_level=40, push_access_level=40, unprotect_access_level=40)
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

