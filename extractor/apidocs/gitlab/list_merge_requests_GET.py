import requests, json
from urllib.parse import quote


def list_merge_requests(state=None, scope='created_by_me', author_id=None, author_username=None, labels=None, milestone=None, my_reaction_emoji=None, search=None, in='title,description'):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/merge_requests"
    querystring = {'state': state, 'scope': scope, 'author_id': author_id, 'author_username': author_username, 'labels': labels, 'milestone': milestone, 'my_reaction_emoji': my_reaction_emoji, 'search': search, 'in': in, }
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
    r = list_merge_requests(state='''opened''', scope='''all''', author_id=5, author_username='''gitlab-bot''', labels='''bug,reproduced''', milestone='''release''', my_reaction_emoji='''star''', search='''foo''', in='''title''')
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

