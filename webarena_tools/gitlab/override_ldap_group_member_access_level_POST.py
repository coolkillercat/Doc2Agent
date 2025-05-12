import requests
from urllib.parse import quote
                
def override_ldap_group_member_access_level(id=None, user_id=None):
    api_url = f"/api/v4/groups/{id}/members/{user_id}/override"
    payload = {'id': id, 'user_id': user_id, }
    assert id is not None, 'Missing required parameter: id'
    assert user_id is not None, 'Missing required parameter: user_id'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = override_ldap_group_member_access_level(id='''123''', user_id='''789''')
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

