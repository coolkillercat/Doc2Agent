import requests, json
from urllib.parse import quote


def create_a_group_deploy_token(id=None, name=None, scopes=None, expires_at=None, username=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/:id/deploy_tokens"
    payload = {'id': id, 'name': name, 'scopes': scopes, 'expires_at': expires_at, 'username': username, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert name is not None, 'Missing required parameter: name'
    assert scopes is not None, 'Missing required parameter: scopes'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_group_deploy_token(id=5, name='''My deploy token''', scopes=['read_repository'], expires_at=2021-01-01T00:00:00Z, username='''custom-user''')
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

