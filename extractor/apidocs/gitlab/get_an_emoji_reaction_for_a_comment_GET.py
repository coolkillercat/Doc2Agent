import requests, json
from urllib.parse import quote


def get_an_emoji_reaction_for_a_comment(id=None, issue_iid=None, note_id=None, award_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/issues/{quote(issue_iid, safe='')}/notes/{quote(note_id, safe='')}/award_emoji/{quote(award_id, safe='')}"
    querystring = {'id': id, 'issue_iid': issue_iid, 'note_id': note_id, 'award_id': award_id, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert issue_iid is not None, 'Missing required parameter: issue_iid'
    assert note_id is not None, 'Missing required parameter: note_id'
    assert award_id is not None, 'Missing required parameter: award_id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_an_emoji_reaction_for_a_comment(id=1, issue_iid=80, note_id=1, award_id=2)
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

