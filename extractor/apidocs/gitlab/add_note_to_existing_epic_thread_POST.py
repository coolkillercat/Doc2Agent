import requests, json
from urllib.parse import quote


def add_note_to_existing_epic_thread(body=None, discussion_id=None, epic_id=None, id=None, note_id=None, created_at=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/:id/epics/:epic_id/discussions/:discussion_id/notes"
    payload = {'body': body, 'discussion_id': discussion_id, 'epic_id': epic_id, 'id': id, 'note_id': note_id, 'created_at': created_at, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert body is not None, 'Missing required parameter: body'
    assert discussion_id is not None, 'Missing required parameter: discussion_id'
    assert epic_id is not None, 'Missing required parameter: epic_id'
    assert id is not None, 'Missing required parameter: id'
    assert note_id is not None, 'Missing required parameter: note_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_note_to_existing_epic_thread(body='''This is a note.''', discussion_id=636, epic_id=11, id=5, note_id=1108, created_at='''2016-03-11T03:45:40Z''')
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

