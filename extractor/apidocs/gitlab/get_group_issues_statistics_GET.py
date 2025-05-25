import requests, json
from urllib.parse import quote


def get_group_issues_statistics(id=None, labels=None, iids__=None, milestone=None, scope=None, author_id=None, author_username=None, assignee_id=None, assignee_username=None, my_reaction_emoji=None, search=None, created_after=None, created_before=None, updated_after=None, updated_before=None, confidential=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/{quote(id, safe='')}/issues_statistics"
    querystring = {'id': id, 'labels': labels, 'iids__': iids__, 'milestone': milestone, 'scope': scope, 'author_id': author_id, 'author_username': author_username, 'assignee_id': assignee_id, 'assignee_username': assignee_username, 'my_reaction_emoji': my_reaction_emoji, 'search': search, 'created_after': created_after, 'created_before': created_before, 'updated_after': updated_after, 'updated_before': updated_before, 'confidential': confidential, }
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
    r = get_group_issues_statistics(id=4, labels='''bug,feature''', iids__=[42, 43], milestone='''1.0.0''', scope='''all''', author_id=5, author_username='''johndoe''', assignee_id=5, assignee_username=['janedoe'], my_reaction_emoji='''star''', search='''bug fix''', created_after=2019-03-15T08:00:00Z, created_before=2019-03-15T08:00:00Z, updated_after=2019-03-15T08:00:00Z, updated_before=2019-03-15T08:00:00Z, confidential=True)
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

