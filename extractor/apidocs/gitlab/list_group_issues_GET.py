import requests, json
from urllib.parse import quote


def list_group_issues(id=None, assignee_id=None, author_id=None, confidential=None, iids__=None, labels=None, milestone=None, my_reaction_emoji=None, state=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/{quote(id, safe='')}/issues"
    querystring = {'id': id, 'assignee_id': assignee_id, 'author_id': author_id, 'confidential': confidential, 'iids__': iids__, 'labels': labels, 'milestone': milestone, 'my_reaction_emoji': my_reaction_emoji, 'state': state, }
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
    r = list_group_issues(id=4, assignee_id=5, author_id=5, confidential=true, iids__=[42, 43], labels='''foo,bar''', milestone='''1.0.0''', my_reaction_emoji='''star''', state='''opened''')
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

