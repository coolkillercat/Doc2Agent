import requests, json
from urllib.parse import quote


def create_new_epic_note(id=None, epic_id=None, body=None, confidential=None, internal=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/:id/epics/:epic_id/notes"
    payload = {'id': id, 'epic_id': epic_id, 'body': body, 'confidential': confidential, 'internal': internal, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert epic_id is not None, 'Missing required parameter: epic_id'
    assert body is not None, 'Missing required parameter: body'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_epic_note(id=5, epic_id=11, body='''This is an epic note.''', confidential=True, internal=True)
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

