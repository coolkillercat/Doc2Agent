import requests, json
from urllib.parse import quote


def create_new_merge_request_thread(body=None, id=None, merge_request_iid=None, position_base_sha_=None, position_head_sha_=None, position_start_sha_=None, position_new_path_=None, position_old_path_=None, position_position_type_=None, commit_id=None, created_at=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/:id/merge_requests/:merge_request_iid/discussions"
    payload = {'body': body, 'id': id, 'merge_request_iid': merge_request_iid, 'position_base_sha_': position_base_sha_, 'position_head_sha_': position_head_sha_, 'position_start_sha_': position_start_sha_, 'position_new_path_': position_new_path_, 'position_old_path_': position_old_path_, 'position_position_type_': position_position_type_, 'commit_id': commit_id, 'created_at': created_at, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert body is not None, 'Missing required parameter: body'
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_new_merge_request_thread(body='''This is a new merge request discussion.''', id=5, merge_request_iid=11, position_base_sha_='''b5d6e7b1613fca24d250fa8e5bc7bcc3dd6002ef''', position_head_sha_='''4803c71e6b1833ca72b8b26ef2ecd5adc8a38031''', position_start_sha_='''7c9c2ead8a320fb7ba0b4e234bd9529a2614e306''', position_new_path_='''file.js''', position_old_path_='''file.js''', position_position_type_='''text''', commit_id='''4803c71e6b1833ca72b8b26ef2ecd5adc8a38031''', created_at='''2016-03-11T03:45:40Z''')
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

