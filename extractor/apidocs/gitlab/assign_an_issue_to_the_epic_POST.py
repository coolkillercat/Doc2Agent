import requests, json
from urllib.parse import quote


def assign_an_issue_to_the_epic(id=None, epic_iid=None, issue_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/groups/:id/epics/:epic_iid/issues/:issue_id"
    payload = {'id': id, 'epic_iid': epic_iid, 'issue_id': issue_id, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert epic_iid is not None, 'Missing required parameter: epic_iid'
    assert issue_id is not None, 'Missing required parameter: issue_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = assign_an_issue_to_the_epic(id=1, epic_iid=5, issue_id=55)
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

