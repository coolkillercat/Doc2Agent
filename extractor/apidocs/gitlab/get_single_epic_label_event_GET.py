import requests, json
from urllib.parse import quote


def get_single_epic_label_event(id=None, epic_id=None, resource_label_event_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/{quote(id, safe='')}/epics/{quote(epic_id, safe='')}/resource_label_events/{quote(resource_label_event_id, safe='')}"
    querystring = {'id': id, 'epic_id': epic_id, 'resource_label_event_id': resource_label_event_id, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert epic_id is not None, 'Missing required parameter: epic_id'
    assert resource_label_event_id is not None, 'Missing required parameter: resource_label_event_id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_single_epic_label_event(id=1, epic_id=11, resource_label_event_id=107)
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

