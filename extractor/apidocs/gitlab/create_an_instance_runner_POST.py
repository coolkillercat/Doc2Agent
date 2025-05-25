import requests, json
from urllib.parse import quote


def create_an_instance_runner(token=None, description=None, info=None, paused=None, locked=None, run_untagged=None, tag_list=None, access_level=None, maximum_timeout=None, maintenance_note=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/runners"
    payload = {'token': token, 'description': description, 'info': info, 'paused': paused, 'locked': locked, 'run_untagged': run_untagged, 'tag_list': tag_list, 'access_level': access_level, 'maximum_timeout': maximum_timeout, 'maintenance_note': maintenance_note, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert token is not None, 'Missing required parameter: token'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_an_instance_runner(token='''<registration_token>''', description='''test-1-20150125-test''', info={'version': '14.0', 'platform': 'linux', 'architecture': 'x86_64'}, paused=False, locked=False, run_untagged=True, tag_list=['ruby', 'mysql', 'tag1', 'tag2'], access_level='''ref_protected''', maximum_timeout=3600, maintenance_note='''Routine maintenance''')
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

