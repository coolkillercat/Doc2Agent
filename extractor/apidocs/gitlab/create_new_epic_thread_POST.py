import requests, json
from urllib.parse import quote


def create_new_epic_thread(body=None, epic_id=None, id=None, created_at=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/:id/epics/:epic_id/discussions"
    payload = {'body': body, 'epic_id': epic_id, 'id': id, 'created_at': created_at, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert body is not None, 'Missing required parameter: body'
    assert epic_id is not None, 'Missing required parameter: epic_id'
    assert id is not None, 'Missing required parameter: id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_epic_thread(body='''This is a new epic discussion.''', epic_id=11, id=5, created_at='''2016-03-11T03:45:40Z''')
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

