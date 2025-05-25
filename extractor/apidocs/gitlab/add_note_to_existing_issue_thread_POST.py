import requests, json
from urllib.parse import quote


def add_note_to_existing_issue_thread(body=None, discussion_id=None, id=None, issue_iid=None, note_id=None, created_at=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/issues/:issue_iid/discussions/:discussion_id/notes"
    payload = {'body': body, 'discussion_id': discussion_id, 'id': id, 'issue_iid': issue_iid, 'note_id': note_id, 'created_at': created_at, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert body is not None, 'Missing required parameter: body'
    assert discussion_id is not None, 'Missing required parameter: discussion_id'
    assert id is not None, 'Missing required parameter: id'
    assert issue_iid is not None, 'Missing required parameter: issue_iid'
    assert note_id is not None, 'Missing required parameter: note_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_note_to_existing_issue_thread(body='''This is a note.''', discussion_id=636, id=5, issue_iid=11, note_id=1108, created_at='''2016-03-11T03:45:40Z''')
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

