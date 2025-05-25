import requests, json
from urllib.parse import quote


def create_ssh_certificate(id=None, key=None, title=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/:id/ssh_certificates"
    payload = {'id': id, 'key': key, 'title': title, }
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
    r = create_ssh_certificate(id=5, key='''ssh-rsa AAAAB3NzaC1ea2dAAAADAQABAAAAgQDGbLkF44ScxRQi2FfA7VsHgGqptguSbmW26jkJhEiRZpGS4/+UzaaSqc8Psw2OhSsKc5QwfrB/ANpO4LhOjDzhf2FuD8ACkv3R7XtaJ+rN6PlyzoBfLAiSyzxhEoMFDBprTgaiZKgg2yQ9dRH55w3f6XMZ4hnaUae53nQgfQLxFw== example@gitlab.com''', title='''newtitle''')
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

