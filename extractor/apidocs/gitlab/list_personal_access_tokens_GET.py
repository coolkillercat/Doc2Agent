import requests, json
from urllib.parse import quote


def list_personal_access_tokens(created_after=None, created_before=None, last_used_after=None, last_used_before=None, revoked=None, search=None, state=None, user_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/personal_access_tokens"
    querystring = {'created_after': created_after, 'created_before': created_before, 'last_used_after': last_used_after, 'last_used_before': last_used_before, 'revoked': revoked, 'search': search, 'state': state, 'user_id': user_id, }
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
    r = list_personal_access_tokens(created_after=2022-01-01T00:00:00, created_before=2022-01-01T00:00:00, last_used_after=2022-01-01T00:00:00, last_used_before=2022-01-01T00:00:00, revoked=true, search='''name''', state='''inactive''', user_id=1)
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

