import requests, json
from urllib.parse import quote


def get_issues_statistics(labels=None, milestone=None, scope=None, author_id=None, author_username=None, assignee_id=None, assignee_username=None, epic_id=None, my_reaction_emoji=None, iids__=None, search=None, in=None, created_after=None, created_before=None, updated_after=None, updated_before=None, confidential=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/issues_statistics"
    querystring = {'labels': labels, 'milestone': milestone, 'scope': scope, 'author_id': author_id, 'author_username': author_username, 'assignee_id': assignee_id, 'assignee_username': assignee_username, 'epic_id': epic_id, 'my_reaction_emoji': my_reaction_emoji, 'iids__': iids__, 'search': search, 'in': in, 'created_after': created_after, 'created_before': created_before, 'updated_after': updated_after, 'updated_before': updated_before, 'confidential': confidential, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_issues_statistics(labels='''bug,feature''', milestone='''1.0.0''', scope='''all''', author_id=5, author_username='''johndoe''', assignee_id=5, assignee_username=['janedoe'], epic_id=10, my_reaction_emoji='''star''', iids__=[42, 43], search='''bug fix''', in='''title''', created_after=2019-03-15T08:00:00Z, created_before=2019-03-15T08:00:00Z, updated_after=2019-03-15T08:00:00Z, updated_before=2019-03-15T08:00:00Z, confidential=True)
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

