import requests, json
from urllib.parse import quote


def create_a_related_epic_link(epic_iid=None, id=None, target_epic_iid=None, target_group_id=None, link_type=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/:id/epics/:epic_iid/related_epics"
    payload = {'epic_iid': epic_iid, 'id': id, 'target_epic_iid': target_epic_iid, 'target_group_id': target_group_id, 'link_type': link_type, }
    headers = {
        "Authorization": "Bearer " + "GITLAB_KEY_REMOVED",
        "PRIVATE-TOKEN": "GITLAB_KEY_REMOVED",
        "Private-Token": "GITLAB_KEY_REMOVED",
    }
    assert epic_iid is not None, 'Missing required parameter: epic_iid'
    assert id is not None, 'Missing required parameter: id'
    assert target_epic_iid is not None, 'Missing required parameter: target_epic_iid'
    assert target_group_id is not None, 'Missing required parameter: target_group_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_related_epic_link(epic_iid=1, id=26, target_epic_iid=5, target_group_id=26, link_type='''relates_to''')
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

