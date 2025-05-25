import requests, json
from urllib.parse import quote


def create_new_epic(id=None, title=None, labels=None, description=None, color=None, confidential=None, created_at=None, start_date_is_fixed=None, start_date_fixed=None, due_date_is_fixed=None, due_date_fixed=None, parent_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/:id/epics"
    payload = {'id': id, 'title': title, 'labels': labels, 'description': description, 'color': color, 'confidential': confidential, 'created_at': created_at, 'start_date_is_fixed': start_date_is_fixed, 'start_date_fixed': start_date_fixed, 'due_date_is_fixed': due_date_is_fixed, 'due_date_fixed': due_date_fixed, 'parent_id': parent_id, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert title is not None, 'Missing required parameter: title'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_epic(id=1, title='''New Epic''', labels='''feature,urgent''', description='''This is a detailed description of the epic.''', color='''#FF5733''', confidential=False, created_at='''2016-03-11T03:45:40Z''', start_date_is_fixed=True, start_date_fixed='''2023-01-01''', due_date_is_fixed=True, due_date_fixed='''2023-12-31''', parent_id=29)
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

