import requests, json
from urllib.parse import quote


def create_external_status_check_service(id=None, name=None, external_url=None, protected_branch_ids=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/external_status_checks"
    payload = {'id': id, 'name': name, 'external_url': external_url, 'protected_branch_ids': protected_branch_ids, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    assert external_url is not None, 'Missing required parameter: external_url'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_external_status_check_service(id=1, name='''Compliance Tool''', external_url='''https://gitlab.com/example/compliance-tool''', protected_branch_ids=[14])
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

