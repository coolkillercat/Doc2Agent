import requests, json
from urllib.parse import quote


def list_all_members_of_a_group_or_project_including_inherited_and_invited_members(id=None, query=None, user_ids=None, show_seat_info=None, state=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(id, safe='')}/members/all"
    querystring = {'id': id, 'query': query, 'user_ids': user_ids, 'show_seat_info': show_seat_info, 'state': state, }
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
    r = list_all_members_of_a_group_or_project_including_inherited_and_invited_members(id=123, query='''john''', user_ids=[1, 2, 3], show_seat_info=true, state='''active''')
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

