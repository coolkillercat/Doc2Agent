import requests, json
from urllib.parse import quote


def create_a_board_list(id=None, board_id=None, label_id=None, assignee_id=None, milestone_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/boards/:board_id/lists"
    payload = {'id': id, 'board_id': board_id, 'label_id': label_id, 'assignee_id': assignee_id, 'milestone_id': milestone_id, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert board_id is not None, 'Missing required parameter: board_id'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_a_board_list(id=5, board_id=1, label_id=5, assignee_id=1, milestone_id=43)
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

