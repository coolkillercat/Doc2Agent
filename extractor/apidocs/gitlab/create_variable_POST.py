import requests, json
from urllib.parse import quote


def create_variable(id=None, key=None, value=None, description=None, environment_scope=None, masked=None, protected=None, raw=None, variable_type=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/:id/variables"
    payload = {'id': id, 'key': key, 'value': value, 'description': description, 'environment_scope': environment_scope, 'masked': masked, 'protected': protected, 'raw': raw, 'variable_type': variable_type, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert key is not None, 'Missing required parameter: key'
    assert value is not None, 'Missing required parameter: value'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_variable(id=1, key='''NEW_VARIABLE''', value='''new value''', description='''null''', environment_scope='''*''', masked=false, protected=false, raw=false, variable_type='''env_var''')
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

