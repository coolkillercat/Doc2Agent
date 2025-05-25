import requests, json
from urllib.parse import quote


def add_deploy_key(id=None, key=None, title=None, can_push=None, expires_at=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/deploy_keys"
    payload = {'id': id, 'key': key, 'title': title, 'can_push': can_push, 'expires_at': expires_at, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert key is not None, 'Missing required parameter: key'
    assert title is not None, 'Missing required parameter: title'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_deploy_key(id=5, key='''ssh-rsa AAAA...''', title='''My deploy key''', can_push=true, expires_at=2019-03-15T08:00:00Z)
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

