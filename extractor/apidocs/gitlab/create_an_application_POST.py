import requests, json
from urllib.parse import quote


def create_an_application(name=None, redirect_uri=None, scopes=None, confidential=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/applications"
    payload = {'name': name, 'redirect_uri': redirect_uri, 'scopes': scopes, 'confidential': confidential, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert name is not None, 'Missing required parameter: name'
    assert redirect_uri is not None, 'Missing required parameter: redirect_uri'
    assert scopes is not None, 'Missing required parameter: scopes'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_an_application(name='''MyApplication''', redirect_uri='''http://redirect.uri''', scopes='''api read_user email''', confidential=True)
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

