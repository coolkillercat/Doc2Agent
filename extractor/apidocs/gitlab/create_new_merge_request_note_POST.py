import requests, json
from urllib.parse import quote


def create_new_merge_request_note(id=None, merge_request_iid=None, body=None, created_at=None, merge_request_diff_head_sha=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/merge_requests/:merge_request_iid/notes"
    payload = {'id': id, 'merge_request_iid': merge_request_iid, 'body': body, 'created_at': created_at, 'merge_request_diff_head_sha': merge_request_diff_head_sha, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    assert body is not None, 'Missing required parameter: body'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_merge_request_note(id=5, merge_request_iid=11, body='''This is a merge request note.''', created_at='''2016-03-11T03:45:40Z''', merge_request_diff_head_sha='''abc123def456''')
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

