import requests, json
from urllib.parse import quote


def add_a_new_emoji_reaction(id=None, issue_iid___merge_request_iid___snippet_id=None, name=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/issues/:issue_iid/award_emoji"
    payload = {'id': id, 'issue_iid___merge_request_iid___snippet_id': issue_iid___merge_request_iid___snippet_id, 'name': name, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert issue_iid___merge_request_iid___snippet_id is not None, 'Missing required parameter: issue_iid___merge_request_iid___snippet_id'
    assert name is not None, 'Missing required parameter: name'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_a_new_emoji_reaction(id=1, issue_iid___merge_request_iid___snippet_id=80, name='''blowfish''')
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

