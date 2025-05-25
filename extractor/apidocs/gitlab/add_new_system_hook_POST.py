import requests, json
from urllib.parse import quote


def add_new_system_hook(url=None, token=None, push_events=None, tag_push_events=None, merge_requests_events=None, repository_update_events=None, enable_ssl_verification=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/hooks"
    payload = {'url': url, 'token': token, 'push_events': push_events, 'tag_push_events': tag_push_events, 'merge_requests_events': merge_requests_events, 'repository_update_events': repository_update_events, 'enable_ssl_verification': enable_ssl_verification, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert url is not None, 'Missing required parameter: url'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_new_system_hook(url='''http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/hook''', token='''secretToken123''', push_events=True, tag_push_events=False, merge_requests_events=True, repository_update_events=True, enable_ssl_verification=True)
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

