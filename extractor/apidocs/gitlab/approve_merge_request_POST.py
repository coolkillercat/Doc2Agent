import requests, json
from urllib.parse import quote


def approve_merge_request(id=None, merge_request_iid=None, approval_password=None, sha=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/merge_requests/:merge_request_iid/approve"
    payload = {'id': id, 'merge_request_iid': merge_request_iid, 'approval_password': approval_password, 'sha': sha, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = approve_merge_request(id=1, merge_request_iid=5, approval_password='''password123''', sha='''abc123''')
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

