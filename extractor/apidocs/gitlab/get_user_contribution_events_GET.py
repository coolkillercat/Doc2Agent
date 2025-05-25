import requests, json
from urllib.parse import quote


def get_user_contribution_events(id=None, action=None, target_type=None, before=None, after=None, sort=None, page=None, per_page=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/users/{quote(id, safe='')}/events"
    querystring = {'id': id, 'action': action, 'target_type': target_type, 'before': before, 'after': after, 'sort': sort, 'page': page, 'per_page': per_page, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_user_contribution_events(id=1, action='''closed''', target_type='''issue''', before=2017-03-01, after=2017-01-31, sort='''desc''', page=1, per_page=20)
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

