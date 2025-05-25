import requests, json
from urllib.parse import quote


def get_single_merge_request_milestone_event(id=None, merge_request_iid=None, resource_milestone_event_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/{quote(id, safe='')}/merge_requests/{quote(merge_request_iid, safe='')}/resource_milestone_events/{quote(resource_milestone_event_id, safe='')}"
    querystring = {'id': id, 'merge_request_iid': merge_request_iid, 'resource_milestone_event_id': resource_milestone_event_id, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    assert resource_milestone_event_id is not None, 'Missing required parameter: resource_milestone_event_id'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_single_merge_request_milestone_event(id=5, merge_request_iid=11, resource_milestone_event_id=120)
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

