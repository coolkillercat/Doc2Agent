import requests, json
from urllib.parse import quote


def add_a_member_to_a_group_or_project(id=None, user_id=None, access_level=None, expires_at=None, invite_source=None, member_role_id=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/groups/:id/members"
    payload = {'id': id, 'user_id': user_id, 'access_level': access_level, 'expires_at': expires_at, 'invite_source': invite_source, 'member_role_id': member_role_id, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert user_id is not None, 'Missing required parameter: user_id'
    assert access_level is not None, 'Missing required parameter: access_level'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = add_a_member_to_a_group_or_project(id=123, user_id=1, access_level=30, expires_at='''2023-12-31''', invite_source='''web''', member_role_id=5)
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

