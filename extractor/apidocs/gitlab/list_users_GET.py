import requests, json
from urllib.parse import quote


def list_users(username=None, search=None, active=None, external=None, exclude_external=None, blocked=None, created_after=None, created_before=None, exclude_internal=None, without_project_bots=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/users"
    querystring = {'username': username, 'search': search, 'active': active, 'external': external, 'exclude_external': exclude_external, 'blocked': blocked, 'created_after': created_after, 'created_before': created_before, 'exclude_internal': exclude_internal, 'without_project_bots': without_project_bots, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_users(username='''john_doe''', search='''john''', active=True, external=True, exclude_external=True, blocked=True, created_after=2023-01-01T00:00:00Z, created_before=2023-12-31T23:59:59Z, exclude_internal=True, without_project_bots=True)
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

